"""Génère corpus/index/index.json à partir des fiches du corpus.

Usage :
    python scripts/generer_index.py           # écrit l'index
    python scripts/generer_index.py --check   # vérifie seulement qu'il est à jour (pour la CI)

L'index ne contient aucune date de génération : il ne change que si le corpus change.
Ne jamais modifier index.json à la main.
"""

from __future__ import annotations

import argparse
import json
import sys

from corpus_lib import FICHIER_INDEX, charger_corpus, configurer_sortie, niveaux_par_type


def construire_index() -> dict:
    corpus = charger_corpus()
    niveaux = niveaux_par_type(corpus.types_sources)
    sources = [f for f in corpus.sources if f.id and not f.erreur_lecture]
    faits = [f for f in corpus.faits if f.id and not f.erreur_lecture]

    cite_par: dict[str, list[str]] = {}
    for f in faits:
        for s in f.entete.get("sources") or []:
            if isinstance(s, dict) and s.get("source"):
                cite_par.setdefault(s["source"], []).append(f.id)

    entrees_sources = []
    for f in sorted(sources, key=lambda x: x.id):
        e = f.entete
        entrees_sources.append(
            {
                "id": f.id,
                "chemin": f.chemin_relatif,
                "titre": e.get("titre"),
                "editeur": e.get("editeur"),
                "type": e.get("type"),
                "niveau": niveaux.get(e.get("type")),
                "date_publication": e.get("date_publication"),
                "themes": e.get("themes") or [],
                "sous_themes": e.get("sous_themes") or [],
                "pays": e.get("pays") or [],
                "url": e.get("url"),
                "depend_de": e.get("depend_de") or [],
                "cite_par": sorted(cite_par.get(f.id, [])),
            }
        )

    entrees_faits = []
    for f in sorted(faits, key=lambda x: x.id):
        e = f.entete
        entrees_faits.append(
            {
                "id": f.id,
                "chemin": f.chemin_relatif,
                "enonce": e.get("enonce"),
                "periode": e.get("periode"),
                "statut": e.get("statut"),
                "date_validite": e.get("date_validite"),
                "themes": e.get("themes") or [],
                "sous_themes": e.get("sous_themes") or [],
                "pays": e.get("pays") or [],
                "sources": [s.get("source") for s in e.get("sources") or [] if isinstance(s, dict)],
            }
        )

    par_theme: dict[str, dict[str, list[str]]] = {
        t: {"sources": [], "faits": []} for t in (corpus.taxonomie.get("themes") or {})
    }
    for cle, entrees in (("sources", entrees_sources), ("faits", entrees_faits)):
        for entree in entrees:
            for theme in entree["themes"]:
                par_theme.setdefault(theme, {"sources": [], "faits": []})[cle].append(entree["id"])

    return {
        "avertissement": "Fichier généré par scripts/generer_index.py. Ne pas modifier à la main.",
        "statistiques": {
            "sources": len(entrees_sources),
            "faits": len(entrees_faits),
            "faits_valides": sum(1 for f in entrees_faits if f["statut"] == "valide"),
        },
        "par_theme": par_theme,
        "sources": entrees_sources,
        "faits": entrees_faits,
    }


def serialiser(index: dict) -> str:
    return json.dumps(index, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    configurer_sortie()
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="vérifie que l'index est à jour sans l'écrire")
    args = parser.parse_args()

    contenu = serialiser(construire_index())
    if args.check:
        actuel = FICHIER_INDEX.read_text(encoding="utf-8") if FICHIER_INDEX.exists() else ""
        if actuel != contenu:
            print("ERREUR : corpus/index/index.json n'est pas à jour. Lancez : python scripts/generer_index.py")
            return 1
        print("Index à jour.")
        return 0

    FICHIER_INDEX.parent.mkdir(parents=True, exist_ok=True)
    with FICHIER_INDEX.open("w", encoding="utf-8", newline="\n") as f:
        f.write(contenu)
    print(f"Index écrit : {FICHIER_INDEX.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
