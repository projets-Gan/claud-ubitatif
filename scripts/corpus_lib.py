"""Fonctions communes pour lire le corpus et la configuration.

Utilisé par valider_corpus.py et generer_index.py. Aucune clé API, aucun accès réseau.
"""

from __future__ import annotations

import datetime as _dt
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
DOSSIER_CORPUS = RACINE / "corpus"
DOSSIER_SOURCES = DOSSIER_CORPUS / "sources"
DOSSIER_FAITS = DOSSIER_CORPUS / "faits"
FICHIER_INDEX = DOSSIER_CORPUS / "index" / "index.json"


def configurer_sortie() -> None:
    """Force l'UTF-8 sur la sortie (utile sous Windows)."""
    for flux in (sys.stdout, sys.stderr):
        try:
            flux.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def _dates_en_texte(valeur):
    """YAML convertit 2026-10-28 en objet date : on le remet en texte ISO."""
    if isinstance(valeur, (_dt.date, _dt.datetime)):
        return valeur.isoformat()[:10]
    if isinstance(valeur, dict):
        return {k: _dates_en_texte(v) for k, v in valeur.items()}
    if isinstance(valeur, list):
        return [_dates_en_texte(v) for v in valeur]
    return valeur


def charger_yaml(chemin: Path):
    with chemin.open(encoding="utf-8") as f:
        return _dates_en_texte(yaml.safe_load(f))


def charger_json(chemin: Path):
    with chemin.open(encoding="utf-8") as f:
        return json.load(f)


@dataclass
class Fiche:
    chemin: Path
    entete: dict
    corps: str
    erreur_lecture: str | None = None

    @property
    def id(self) -> str | None:
        return self.entete.get("id") if isinstance(self.entete, dict) else None

    @property
    def chemin_relatif(self) -> str:
        return self.chemin.relative_to(RACINE).as_posix()


def lire_fiche(chemin: Path) -> Fiche:
    """Lit un fichier Markdown avec en-tête YAML délimité par des lignes '---'."""
    texte = chemin.read_text(encoding="utf-8")
    if texte.startswith("﻿"):
        texte = texte[1:]
    lignes = texte.splitlines()
    if not lignes or lignes[0].strip() != "---":
        return Fiche(chemin, {}, texte, "l'en-tête YAML doit commencer par une ligne '---'")
    try:
        fin = next(i for i in range(1, len(lignes)) if lignes[i].strip() == "---")
    except StopIteration:
        return Fiche(chemin, {}, texte, "l'en-tête YAML n'est pas fermé par une ligne '---'")
    try:
        entete = _dates_en_texte(yaml.safe_load("\n".join(lignes[1:fin]))) or {}
    except yaml.YAMLError as exc:
        return Fiche(chemin, {}, texte, f"YAML invalide : {exc}")
    if not isinstance(entete, dict):
        return Fiche(chemin, {}, texte, "l'en-tête YAML doit être un dictionnaire clé: valeur")
    corps = "\n".join(lignes[fin + 1 :]).strip()
    return Fiche(chemin, entete, corps)


def lister_fichiers(dossier: Path) -> list[Path]:
    if not dossier.exists():
        return []
    return sorted(p for p in dossier.rglob("*") if p.is_file() and p.name != ".gitkeep")


@dataclass
class Corpus:
    taxonomie: dict
    types_sources: dict
    sources: list[Fiche] = field(default_factory=list)
    faits: list[Fiche] = field(default_factory=list)
    fichiers_inattendus: list[Path] = field(default_factory=list)


def charger_corpus() -> Corpus:
    corpus = Corpus(
        taxonomie=charger_yaml(RACINE / "config" / "taxonomie.yaml"),
        types_sources=charger_yaml(RACINE / "config" / "types-sources.yaml"),
    )
    for dossier, cible in ((DOSSIER_SOURCES, corpus.sources), (DOSSIER_FAITS, corpus.faits)):
        for chemin in lister_fichiers(dossier):
            if chemin.suffix != ".md":
                corpus.fichiers_inattendus.append(chemin)
                continue
            cible.append(lire_fiche(chemin))
    return corpus


def origines(id_source: str, sources_par_id: dict[str, Fiche], _vus: frozenset = frozenset()) -> set[str]:
    """Sources « racines » dont dépend une source (elle-même si elle ne reprend rien)."""
    fiche = sources_par_id.get(id_source)
    if fiche is None or id_source in _vus:
        return {id_source}
    parents = fiche.entete.get("depend_de") or []
    if not parents:
        return {id_source}
    resultat: set[str] = set()
    for parent in parents:
        resultat |= origines(parent, sources_par_id, _vus | {id_source})
    return resultat


def sont_independantes(a: str, b: str, sources_par_id: dict[str, Fiche]) -> bool:
    """Deux sources sont indépendantes si elles n'ont aucune origine commune
    et ne viennent pas du même éditeur."""
    if a == b:
        return False
    fa, fb = sources_par_id.get(a), sources_par_id.get(b)
    if fa is None or fb is None:
        return False
    editeur_a = str(fa.entete.get("editeur", "")).strip().lower()
    editeur_b = str(fb.entete.get("editeur", "")).strip().lower()
    if editeur_a and editeur_a == editeur_b:
        return False
    return not (origines(a, sources_par_id) & origines(b, sources_par_id))


def nombre_sources_independantes(ids: list[str], sources_par_id: dict[str, Fiche]) -> int:
    """Taille d'un groupe de sources deux à deux indépendantes (calcul glouton)."""
    retenues: list[str] = []
    for i in dict.fromkeys(ids):
        if i in sources_par_id and all(sont_independantes(i, r, sources_par_id) for r in retenues):
            retenues.append(i)
    return len(retenues)
