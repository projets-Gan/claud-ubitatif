"""Liste les faits dont la fraîcheur doit être vérifiée aujourd'hui.

Règles de rythme dans config/veille.yaml. Utilisé par l'agent veilleur.

Usage :
    python scripts/faits_a_verifier.py            # tableau lisible
    python scripts/faits_a_verifier.py --json     # liste JSON (pour l'agent)
    python scripts/faits_a_verifier.py --date 2026-12-01   # simuler une autre date
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys

from corpus_lib import RACINE, charger_corpus, charger_yaml, configurer_sortie


def _date(texte):
    try:
        return dt.date.fromisoformat(str(texte)[:10])
    except (TypeError, ValueError):
        return None


def parametres(veille: dict, themes: list[str]) -> dict:
    p = dict(veille.get("defaut") or {})
    for theme in themes:
        p.update((veille.get("par_theme") or {}).get(theme) or {})
    return p


def faits_dus(corpus, veille: dict, aujourd_hui: dt.date) -> list[dict]:
    dus = []
    for fiche in corpus.faits:
        e = fiche.entete
        if fiche.erreur_lecture or not fiche.id:
            continue
        p = parametres(veille, e.get("themes") or [])
        ajout = _date(e.get("date_ajout"))
        derniere = _date(e.get("date_derniere_verification"))
        validite = _date(e.get("date_validite"))
        raisons, echeance = [], None

        if derniere is None:
            if ajout is not None:
                echeance = ajout + dt.timedelta(hours=int(p.get("delai_premiere_verification_heures", 72)))
                if aujourd_hui >= echeance:
                    raisons.append(f"première vérification (ajouté le {ajout.isoformat()})")
        else:
            echeance = derniere + dt.timedelta(days=int(p.get("intervalle_max_jours", 30)))
            if aujourd_hui >= echeance:
                raisons.append(f"dernière vérification il y a plus de {p.get('intervalle_max_jours', 30)} jours")

        if validite is not None:
            seuil = validite - dt.timedelta(days=int(p.get("anticipation_validite_jours", 7)))
            if aujourd_hui >= seuil and (derniere is None or derniere < seuil):
                raisons.append(
                    "date de validité dépassée" if aujourd_hui > validite else f"date de validité proche ({validite.isoformat()})"
                )
                echeance = min(filter(None, [echeance, seuil]))

        if raisons:
            dus.append(
                {
                    "id": fiche.id,
                    "chemin": fiche.chemin_relatif,
                    "enonce": e.get("enonce"),
                    "statut": e.get("statut"),
                    "date_validite": e.get("date_validite"),
                    "date_derniere_verification": e.get("date_derniere_verification"),
                    "raisons": raisons,
                    "retard_jours": (aujourd_hui - echeance).days if echeance else 0,
                }
            )
    dus.sort(key=lambda d: (-d["retard_jours"], d["id"]))
    return dus


def main() -> int:
    configurer_sortie()
    parser = argparse.ArgumentParser(description="Faits dont la fraîcheur doit être vérifiée")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--date", help="date de référence AAAA-MM-JJ (par défaut aujourd'hui)")
    parser.add_argument("--tous", action="store_true", help="ignorer la limite max_faits_par_passage")
    args = parser.parse_args()

    veille = charger_yaml(RACINE / "config" / "veille.yaml") or {}
    aujourd_hui = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    dus = faits_dus(charger_corpus(), veille, aujourd_hui)
    total = len(dus)
    if not args.tous:
        dus = dus[: int(veille.get("max_faits_par_passage", 15))]

    if args.json:
        print(json.dumps({"date": aujourd_hui.isoformat(), "total_dus": total, "faits": dus}, ensure_ascii=False, indent=2))
        return 0
    print(f"{total} fait(s) à vérifier au {aujourd_hui.isoformat()} ({len(dus)} traité(s) dans ce passage).")
    for d in dus:
        print(f"- {d['id']} : {' ; '.join(d['raisons'])} (retard : {d['retard_jours']} j)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
