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
    nombre_sources_independantes,
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
        if e["statut"] == "valide":
            n = nombre_sources_independantes(ids_sources, sources_par_id)
            if n < 2:
                rapport.erreur(
                    fiche,
                    f"statut « valide » mais seulement {n} source(s) indépendante(s) : il en faut au moins 2 "
                    "(éditeurs différents, sans reprise commune via depend_de)",
                )
        if e["statut"] == "conteste" and not e.get("contredit_par"):
            rapport.erreur(fiche, "statut « conteste » : renseigner contredit_par")
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
