"""Rapport d'impact des règles de validation sur le corpus.

Recalcule, pour chaque fait, ce que permettent les règles EN VIGUEUR
(config/niveaux.yaml et config/types-sources.yaml) et le compare au statut
déclaré dans la fiche. À lancer après toute modification des règles, et
chaque jour par le contrôle automatique.

Usage :
    python scripts/impact_regles.py                    # rapport à l'écran
    python scripts/impact_regles.py --markdown f.md    # rapport écrit dans un fichier
    python scripts/impact_regles.py --appliquer        # repasse en « en-attente » les faits
                                                       # dont le statut « valide » n'est plus justifié

Code de sortie 1 si au moins un fait doit être corrigé, 0 sinon.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

from corpus_lib import charger_corpus, configurer_sortie


def analyser(corpus) -> dict[str, list[dict]]:
    regles = corpus.regles
    sources_par_id = {f.id: f for f in corpus.sources if f.id and not f.erreur_lecture}
    resultat = {"a_corriger": [], "garde_fous": [], "a_reexaminer": []}

    for fiche in corpus.faits:
        e = fiche.entete
        if fiche.erreur_lecture or not isinstance(e.get("sources"), list):
            continue
        ids = [s.get("source") for s in e["sources"] if isinstance(s, dict)]
        bilan = regles.evaluer_validation(ids, sources_par_id)
        niveaux = sorted({str(regles.niveau_source(i, sources_par_id)) for i in ids if i in sources_par_id})
        ligne = {
            "id": fiche.id,
            "chemin": fiche.chemin,
            "statut": e.get("statut"),
            "niveaux": ", ".join(niveaux) or "aucun",
        }
        if e.get("statut") == "valide" and not bilan["valide"]:
            resultat["a_corriger"].append({**ligne, "motif": "statut « valide » non justifié par les règles en vigueur"})
        elif e.get("statut") == "valide" and bilan["source_unique"] and regles.param(bilan["niveau"], "garde_fous"):
            manque = []
            for s in e["sources"]:
                if s.get("source") in bilan["sources_validantes"] and not str(s.get("localisation") or "").strip():
                    manque.append("localisation")
            stats = [i for i in bilan["sources_validantes"] if sources_par_id[i].entete.get("type") == "donnees-officielles"]
            if stats and not e.get("etat_donnee"):
                manque.append("etat_donnee")
            if manque:
                resultat["garde_fous"].append({**ligne, "motif": "source unique : manque " + ", ".join(sorted(set(manque)))})
        elif e.get("statut") == "en-attente" and bilan["valide"]:
            resultat["a_reexaminer"].append(
                {**ligne, "motif": f"pourrait passer « valide » (niveau {bilan['niveau']}) : à confirmer par un humain"}
            )
    return resultat


def rapport_markdown(resultat: dict, version) -> str:
    lignes = [f"# Rapport d'impact des règles (version {version})", ""]
    sections = [
        ("a_corriger", "Faits « valide » qui ne respectent plus les règles", "Ajouter une source, corriger un type, ou repasser en « en-attente » (`--appliquer`)."),
        ("garde_fous", "Faits validés par une source unique sans garde-fous", "Compléter la localisation de l'extrait et/ou etat_donnee."),
        ("a_reexaminer", "Faits « en-attente » qui pourraient être validés", "Information : décision humaine, rien d'automatique."),
    ]
    for cle, titre, conseil in sections:
        lignes += [f"## {titre} ({len(resultat[cle])})", "", conseil, ""]
        if resultat[cle]:
            lignes += ["| Fait | Statut | Niveaux des sources | Motif |", "|---|---|---|---|"]
            lignes += [f"| `{r['id']}` | {r['statut']} | {r['niveaux']} | {r['motif']} |" for r in resultat[cle]]
            lignes.append("")
    return "\n".join(lignes) + "\n"


def appliquer(resultat: dict, version) -> int:
    aujourd_hui = dt.date.today().isoformat()
    n = 0
    for r in resultat["a_corriger"]:
        chemin: Path = r["chemin"]
        texte = chemin.read_text(encoding="utf-8")
        nouveau, k = re.subn(
            r"(?m)^statut:\s*valide\b.*$",
            f"statut: en-attente  # repassé automatiquement le {aujourd_hui} (règles v{version}) : à réexaminer",
            texte,
            count=1,
        )
        if k:
            chemin.write_text(nouveau, encoding="utf-8", newline="\n")
            n += 1
    return n


def main() -> int:
    configurer_sortie()
    parser = argparse.ArgumentParser(description="Rapport d'impact des règles de validation")
    parser.add_argument("--markdown", type=Path, help="écrire le rapport dans ce fichier")
    parser.add_argument("--appliquer", action="store_true", help="repasser en en-attente les faits non justifiés")
    args = parser.parse_args()

    corpus = charger_corpus()
    version = corpus.niveaux.get("version")
    resultat = analyser(corpus)
    texte = rapport_markdown(resultat, version)
    if args.markdown:
        args.markdown.write_text(texte, encoding="utf-8")
    print(texte)

    if args.appliquer:
        n = appliquer(resultat, version)
        print(f"{n} fait(s) repassé(s) en « en-attente ». Relancez ensuite : python scripts/generer_index.py")
        return 0
    return 1 if (resultat["a_corriger"] or resultat["garde_fous"]) else 0


if __name__ == "__main__":
    sys.exit(main())
