"""Valide l'ensemble du corpus.

Usage :
    python scripts/valider_corpus.py

Code de sortie 0 si aucune erreur, 1 sinon. Les avertissements ne bloquent pas.
Lancé automatiquement à chaque Pull Request (voir .github/workflows/validation.yml).
"""

from __future__ import annotations

import datetime as dt
import re
import sys

from jsonschema import Draft202012Validator

from corpus_lib import (
    DOSSIER_FAITS,
    DOSSIER_SOURCES,
    RACINE,
    Fiche,
    charger_corpus,
    charger_json,
    configurer_sortie,
)

MOTIF_NOM = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")


class Rapport:
    def __init__(self) -> None:
        self.erreurs: list[str] = []
        self.avertissements: list[str] = []

    def erreur(self, fiche_ou_chemin, message: str) -> None:
        self.erreurs.append(f"{_nom(fiche_ou_chemin)} : {message}")

    def avertir(self, fiche_ou_chemin, message: str) -> None:
        self.avertissements.append(f"{_nom(fiche_ou_chemin)} : {message}")


def _nom(objet) -> str:
    if isinstance(objet, Fiche):
        return objet.chemin_relatif
    try:
        return objet.relative_to(RACINE).as_posix()
    except (AttributeError, ValueError):
        return str(objet)


def verifier_vocabulaire(fiche: Fiche, corpus, rapport: Rapport) -> None:
    themes_autorises = corpus.taxonomie.get("themes", {})
    pays_autorises = corpus.taxonomie.get("pays", {})
    themes = fiche.entete.get("themes") or []
    for theme in themes:
        if theme not in themes_autorises:
            rapport.erreur(fiche, f"thème inconnu « {theme} » (voir config/taxonomie.yaml)")
    sous_autorises = {
        st for t in themes if t in themes_autorises for st in (themes_autorises[t].get("sous_themes") or {})
    }
    for sous in fiche.entete.get("sous_themes") or []:
        if sous not in sous_autorises:
            rapport.erreur(fiche, f"sous-thème « {sous} » inconnu ou ne relevant d'aucun des thèmes de la fiche")
    for code in fiche.entete.get("pays") or []:
        if code not in pays_autorises:
            rapport.erreur(fiche, f"code pays inconnu « {code} » (voir config/taxonomie.yaml)")


def verifier_emplacement(fiche: Fiche, rapport: Rapport, attendu) -> None:
    if not MOTIF_NOM.match(fiche.chemin.name):
        rapport.erreur(fiche, "nom de fichier invalide (ASCII, minuscules, chiffres et tirets uniquement)")
    if fiche.id and fiche.chemin.stem != fiche.id:
        rapport.erreur(fiche, f"le nom du fichier doit être identique à l'id « {fiche.id} »")
    if attendu is not None and fiche.chemin.parent != attendu:
        rapport.erreur(fiche, f"mauvais dossier, attendu : {_nom(attendu)}/")


def main() -> int:
    configurer_sortie()
    rapport = Rapport()
    corpus = charger_corpus()
    schema_source = Draft202012Validator(charger_json(RACINE / "schemas" / "source.schema.json"))
    schema_fait = Draft202012Validator(charger_json(RACINE / "schemas" / "fait.schema.json"))
    aujourd_hui = dt.date.today().isoformat()

    for chemin in corpus.fichiers_inattendus:
        rapport.erreur(chemin, "seuls des fichiers .md sont autorisés dans corpus/sources et corpus/faits")

    # Identifiants uniques sur l'ensemble du corpus.
    vus: dict[str, Fiche] = {}
    for fiche in corpus.sources + corpus.faits:
        if fiche.id in vus:
            rapport.erreur(fiche, f"id « {fiche.id} » déjà utilisé par {vus[fiche.id].chemin_relatif}")
        elif fiche.id:
            vus[fiche.id] = fiche

    sources_par_id = {f.id: f for f in corpus.sources if f.id and not f.erreur_lecture}
    types_connus = corpus.types_sources.get("types", {})
    regles = corpus.regles

    # --- Configuration des niveaux ----------------------------------------
    chemin_niveaux = RACINE / "config" / "niveaux.yaml"
    for code, niveau in regles.niveau_du_type.items():
        if niveau not in regles.niveaux:
            rapport.erreur(chemin_niveaux, f"le type « {code} » renvoie au niveau « {niveau} », absent de niveaux.yaml")
    if not regles.niveaux_validants():
        rapport.erreur(chemin_niveaux, "aucun niveau ne permet de valider un fait (sources_requises)")

    # --- Liste des sources de niveau 4 -------------------------------------
    chemin_n4 = RACINE / "config" / "sources-niveau-4.yaml"
    editeurs_n4 = {}
    for entree in corpus.sources_niveau_4.get("sources") or []:
        nom = str(entree.get("editeur", "")).strip()
        if not nom:
            rapport.erreur(chemin_n4, "entrée sans editeur")
            continue
        editeurs_n4[nom.lower()] = nom
        preuves = entree.get("preuves") or []
        if len(preuves) < 2:
            rapport.erreur(chemin_n4, f"« {nom} » : au moins 2 preuves (fiches sources du corpus) sont exigées")
        for preuve in preuves:
            if preuve not in sources_par_id:
                rapport.erreur(chemin_n4, f"« {nom} » : preuve « {preuve} » introuvable dans le corpus")
            elif not regles.peut_valider(regles.niveau_source(preuve, sources_par_id)):
                rapport.erreur(chemin_n4, f"« {nom} » : la preuve « {preuve} » doit être une source de niveau validant")
        if not entree.get("criteres"):
            rapport.erreur(chemin_n4, f"« {nom} » : indiquer au moins un critère")

    # --- Sources -----------------------------------------------------------
    for fiche in corpus.sources:
        if fiche.erreur_lecture:
            rapport.erreur(fiche, fiche.erreur_lecture)
            continue
        erreurs_schema = sorted(schema_source.iter_errors(fiche.entete), key=lambda e: list(e.path))
        for e in erreurs_schema:
            champ = ".".join(str(p) for p in e.path) or "(en-tête)"
            rapport.erreur(fiche, f"{champ} : {e.message}")
        if erreurs_schema:
            continue
        e = fiche.entete
        if e["type"] not in types_connus:
            rapport.erreur(fiche, f"type de source inconnu « {e['type']} » (voir config/types-sources.yaml)")
        editeur = str(e["editeur"]).strip().lower()
        if editeur in editeurs_n4 and regles.niveau_du_type.get(e["type"]) != 4:
            rapport.erreur(
                fiche,
                f"l'éditeur « {e['editeur']} » est classé au niveau 4 (config/sources-niveau-4.yaml) : "
                "utiliser le type media-desinformation",
            )
        verifier_vocabulaire(fiche, corpus, rapport)
        attendu = DOSSIER_SOURCES / e["themes"][0] / e["date_publication"][:4]
        verifier_emplacement(fiche, rapport, attendu)
        for parent in e.get("depend_de") or []:
            if parent == fiche.id:
                rapport.erreur(fiche, "une source ne peut pas dépendre d'elle-même")
            elif parent not in sources_par_id:
                rapport.erreur(fiche, f"depend_de : source « {parent} » introuvable dans le corpus")
        if e["date_consultation"] < e["date_publication"]:
            rapport.avertir(fiche, "date_consultation antérieure à date_publication")
        if not e.get("archive"):
            rapport.avertir(fiche, "pas de lien d'archive : à ajouter dès que possible")
        if not fiche.corps:
            rapport.avertir(fiche, "corps vide : ajouter un court résumé de la source")

    # --- Faits -------------------------------------------------------------
    for fiche in corpus.faits:
        if fiche.erreur_lecture:
            rapport.erreur(fiche, fiche.erreur_lecture)
            continue
        erreurs_schema = sorted(schema_fait.iter_errors(fiche.entete), key=lambda e: list(e.path))
        for err in erreurs_schema:
            champ = ".".join(str(p) for p in err.path) or "(en-tête)"
            rapport.erreur(fiche, f"{champ} : {err.message}")
        if erreurs_schema:
            continue
        e = fiche.entete
        verifier_vocabulaire(fiche, corpus, rapport)
        verifier_emplacement(fiche, rapport, DOSSIER_FAITS / e["themes"][0])
        ids_sources = [s["source"] for s in e["sources"]]
        for id_source in ids_sources:
            if id_source not in sources_par_id:
                rapport.erreur(fiche, f"source « {id_source} » introuvable dans le corpus")
        for id_source in e.get("contredit_par") or []:
            if id_source not in sources_par_id:
                rapport.erreur(fiche, f"contredit_par : source « {id_source} » introuvable dans le corpus")
        bilan = regles.evaluer_validation(ids_sources, sources_par_id)
        if e["statut"] == "valide":
            if not bilan["valide"]:
                niveaux_presents = sorted(
                    {str(regles.niveau_source(i, sources_par_id)) for i in ids_sources if i in sources_par_id}
                )
                rapport.erreur(
                    fiche,
                    f"statut « valide » non justifié. Il faut : {regles.resume()}. "
                    f"Niveaux des sources de ce fait : {', '.join(niveaux_presents) or 'aucun'}. "
                    "Les niveaux 3, 4 et bonus ne valident jamais un fait.",
                )
            elif bilan["source_unique"] and regles.param(bilan["niveau"], "garde_fous"):
                # Garde-fous quand une seule source valide le fait.
                for s in e["sources"]:
                    if s["source"] in bilan["sources_validantes"] and not str(s.get("localisation") or "").strip():
                        rapport.erreur(
                            fiche,
                            f"fait validé par une seule source (niveau {bilan['niveau']}) : indiquer la localisation "
                            f"précise de l'extrait de « {s['source']} » (article, tableau, ligne, page…)",
                        )
                stats = [
                    i for i in bilan["sources_validantes"]
                    if sources_par_id[i].entete.get("type") == "donnees-officielles"
                ]
                if stats and not e.get("etat_donnee"):
                    rapport.erreur(
                        fiche,
                        "fait validé par une seule source statistique : renseigner etat_donnee (provisoire ou definitif)",
                    )

        # Contradictions : primauté des niveaux supérieurs, contestation par un niveau validant.
        contradicteurs = [i for i in e.get("contredit_par") or [] if i in sources_par_id]
        niveaux_primaute = [
            n for i in ids_sources
            if regles.est_ordonne(n := regles.niveau_source(i, sources_par_id)) and regles.param(n, "primaute")
        ]
        if e["statut"] == "conteste":
            if not e.get("contredit_par"):
                rapport.erreur(fiche, "statut « conteste » : renseigner contredit_par")
            elif contradicteurs and not any(
                regles.peut_valider(regles.niveau_source(i, sources_par_id)) for i in contradicteurs
            ):
                rapport.erreur(
                    fiche,
                    "statut « conteste » : aucune source contradictoire n'est d'un niveau validant "
                    "(les niveaux 3, 4 et bonus ne suffisent pas à contester un fait)",
                )
            if niveaux_primaute:
                p = min(niveaux_primaute)
                if contradicteurs and not any(
                    regles.est_ordonne(n := regles.niveau_source(i, sources_par_id)) and n <= p
                    for i in contradicteurs
                ):
                    rapport.erreur(
                        fiche,
                        f"fait appuyé sur une source de niveau {p} : il ne peut pas être contesté par des sources "
                        "de niveau inférieur (primauté). Statut attendu : valide.",
                    )

        if e["date_validite"] < aujourd_hui:
            rapport.avertir(fiche, f"date de validité dépassée ({e['date_validite']}) : fait à mettre à jour")

    # --- Bilan -------------------------------------------------------------
    for message in rapport.avertissements:
        print(f"AVERTISSEMENT  {message}")
    for message in rapport.erreurs:
        print(f"ERREUR         {message}")
    print(
        f"\n{len(corpus.sources)} source(s), {len(corpus.faits)} fait(s) : "
        f"{len(rapport.erreurs)} erreur(s), {len(rapport.avertissements)} avertissement(s)."
    )
    return 1 if rapport.erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
