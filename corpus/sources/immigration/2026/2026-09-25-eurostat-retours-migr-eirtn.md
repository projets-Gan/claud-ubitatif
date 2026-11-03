---
id: 2026-09-25-eurostat-retours-migr-eirtn
type_fiche: source
titre: "Third country nationals returned following an order to leave - annual data (rounded) [migr_eirtn]"
editeur: "Eurostat"
auteurs: []
type: donnees-officielles
url: "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/migr_eirtn?geo=FR&citizen=TOTAL&age=TOTAL&sex=T&sinceTimePeriod=2019"
archive: null
hash_sha256: null
date_publication: 2026-09-25
date_consultation: 2026-11-02
themes: [immigration]
sous_themes: [eloignements]
pays: [FR, UE, DE]
langue: en
depend_de: []
notes: >
  Jeu de données Eurostat lu via l'API (JSON-stat), champ « updated » =
  2026-09-25T23:00:00+0200. Valeurs relues par le curateur le 2/11/2026 : FR et DE
  (2023-2025, c_dest=THRD et TOTAL, ordre des dimensions vérifié avec id/size), puis tous
  pays pour c_dest=THRD, time=2025. Rupture de série signalée en 2021 pour la France
  (indicateur « b », relevé par le chercheur et le contradicteur ; hors de la période
  utilisée). Données françaises transmises par le ministère de l'Intérieur (DGEF, DNPAF).
  Archive non créée ; hash non calculé.
---

## Résumé

Série annuelle d'Eurostat sur le nombre de ressortissants de pays tiers effectivement
partis du territoire d'un État membre à la suite d'un ordre de quitter le territoire.
Ventilation par destination : vers un pays tiers (THRD) ou toutes destinations (TOTAL,
y compris vers un autre État membre). Inclut les retours forcés et les retours volontaires
aidés, et les retours volontaires non aidés lorsqu'ils sont enregistrés de façon fiable.
Unité : personnes, valeurs arrondies à 5. Transferts Dublin exclus.

## Extraits

> geo=FR : THRD 2023 : 10620 ; 2024 : 14670 ; 2025 : 14940 — TOTAL 2023 : 12165 ; 2024 : 16665 ; 2025 : 18930.

> geo=DE : THRD 2024 : 18695 ; 2025 : 29295 — TOTAL 2024 : 22005 ; 2025 : 36075.

> c_dest=THRD, 2025 : EU27_2020 : 139270 ; DE : 29295 ; FR : 14940 ; SE : 11250.

## Points d'attention

- Les personnes parties une année peuvent avoir reçu leur ordre de quitter une année
  antérieure : ne pas diviser ces nombres par ceux de migr_eiord pour en faire un « taux ».
- « Retour volontaire » au sens d'Eurostat ≠ « retour aidé » au sens du ministère français.
- Fortes révisions possibles : Allemagne 2024 vers pays tiers = 15 230 dans le communiqué
  Eurostat de mai 2025, 18 695 dans la mise à jour de septembre 2026.
