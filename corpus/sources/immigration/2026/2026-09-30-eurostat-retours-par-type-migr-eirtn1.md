---
id: 2026-09-30-eurostat-retours-par-type-migr-eirtn1
type_fiche: source
titre: "Third-country nationals returned following an order to leave, by type of return, citizenship, country of destination, age and sex - quarterly data [migr_eirtn1]"
editeur: "Eurostat"
auteurs: []
type: donnees-officielles
url: "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/migr_eirtn1?citizen=TOTAL&age=TOTAL&sex=T&c_dest=THRD&return=FORC&sinceTimePeriod=2025-Q1&untilTimePeriod=2025-Q4"
archive: null
hash_sha256: null
date_publication: 2026-09-30
date_consultation: 2026-11-02
themes: [immigration]
sous_themes: [eloignements]
pays: [FR, UE, DE, IT]
langue: en
depend_de: []
notes: >
  Jeu trimestriel Eurostat lu via l'API (JSON-stat), champ « updated » =
  2026-09-30T23:00:00+0200. Valeurs relues par le curateur le 2/11/2026 pour chaque
  trimestre de 2025 et tous pays (return=FORC, c_dest=THRD). Le titre complet du jeu
  n'a été lu que tronqué (« … citizenship, country of destination, age and ») : la fin
  du titre (« sex - quarterly data ») est à confirmer. Le jeu contient aussi le T2 2026 (non utilisé
  ici). Le jeu annuel migr_eirt_vol est vide pour FR et DE de 2023 à 2025 selon le
  contradicteur : la ventilation forcé/volontaire n'est disponible que dans ce jeu
  trimestriel. Archive non créée ; hash non calculé.
---

## Résumé

Série trimestrielle d'Eurostat sur les ressortissants de pays tiers partis à la suite
d'un ordre de quitter le territoire, ventilés par type de retour (forcé, volontaire aidé,
volontaire non aidé) et par destination. Unité : personnes, valeurs arrondies à 5.
Ici utilisée pour les retours **forcés** (return=FORC) **vers un pays tiers** (c_dest=THRD).

## Extraits

> return=FORC, c_dest=THRD, geo=FR : 2025-Q1 : 1700 ; 2025-Q2 : 1555 ; 2025-Q3 : 1435 ; 2025-Q4 : 1495.

> geo=DE : 2025-Q1 : 3625 ; Q2 : 3445 ; Q3 : 3710 ; Q4 : 3370. geo=IT : Q1 : 1245 ; Q2 : 1150 ; Q3 : 1110 ; Q4 : 1270.

> EU27_2020 : Q1 : 13310 ; Q2 : 13115 ; Q3 : 13525 ; Q4 : 13910.

## Points d'attention

- La somme des quatre trimestres arrondis n'est pas une donnée publiée et peut différer
  d'une donnée annuelle.
- Le retour forcé au sens d'Eurostat (« enforced return » : une procédure d'exécution a
  été engagée) ne recouvre pas forcément l'« éloignement forcé » des statistiques du
  ministère de l'Intérieur, qui comprend aussi des ressortissants de l'UE et des
  destinations dans l'UE.
