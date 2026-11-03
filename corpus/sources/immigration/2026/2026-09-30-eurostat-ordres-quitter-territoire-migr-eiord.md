---
id: 2026-09-30-eurostat-ordres-quitter-territoire-migr-eiord
type_fiche: source
titre: "Third country nationals ordered to leave - annual data (rounded) [migr_eiord]"
editeur: "Eurostat"
auteurs: []
type: donnees-officielles
url: "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/migr_eiord?citizen=TOTAL&age=TOTAL&sex=T&sinceTimePeriod=2019"
archive: null
hash_sha256: null
date_publication: 2026-09-30
date_consultation: 2026-11-02
themes: [immigration]
sous_themes: [eloignements]
pays: [FR, UE, DE, ES]
langue: en
depend_de: []
notes: >
  Jeu de données Eurostat lu via l'API de diffusion (format JSON-stat), champ « updated »
  = 2026-09-30T23:00:00+0200 ; date_publication = date de cette mise à jour. Valeurs
  relues par le curateur le 2/11/2026 (requêtes geo=FR 2019-2025, puis tous pays pour
  time=2024 et time=2025). Aucun indicateur de statut (provisoire, estimé) dans la
  réponse. Les données françaises sont transmises par le ministère de l'Intérieur (DGEF) à
  partir des saisies des préfectures (voir 2026-03-23-eurostat-metadonnees-france-migr-eil-sims-fr) :
  Eurostat n'est pas une source indépendante du ministère pour la France. Archive non
  créée (téléchargement direct bloqué par le proxy de l'environnement) ; hash non calculé.
---

## Résumé

Série annuelle d'Eurostat sur le nombre de ressortissants de pays tiers (hors UE, EEE et
Suisse) qui, constatés en séjour irrégulier, font l'objet d'une décision administrative
ou judiciaire leur imposant de quitter le territoire d'un État membre. Unité : personnes,
valeurs arrondies à 5. Données par pays déclarant, toutes nationalités, tous âges, deux
sexes. Les transferts entre États membres (procédure Dublin) sont exclus.

## Extraits

> France (geo=FR), personnes : 2019 : 123845 ; 2020 : 108395 ; 2021 : 125450 ; 2022 : 135645 ; 2023 : 136685 ; 2024 : 128740 ; 2025 : 137550.
> (API, migr_eiord, citizen=TOTAL, age=TOTAL, sex=T, unit=PER, mise à jour du 30/09/2026)

> 2024 : EU27_2020 : 464820 ; ES : 62930 ; DE : 57075 ; EL : 31565 ; IT : 27970.
> 2025 : EU27_2020 : 486705 ; DE : 55240 ; ES : 53700 ; NL : 31230 ; EL : 26635.

## Points d'attention

- Compte des **personnes** ressortissantes de pays tiers, pas des décisions (OQTF) : une
  personne visée par plusieurs mesures dans l'année n'est comptée qu'une fois ; les
  ressortissants de l'UE éloignés par la France ne sont pas compris.
- La métadonnée nationale ne précise pas quelles mesures françaises (OQTF, APRF, ITF,
  expulsion…) sont comptées ni la couverture de l'outre-mer.
- Valeurs révisables : le total UE 2025 est passé de 491 950 (extraction du 29/04/2026,
  Statistics Explained) à 486 705 (mise à jour du 30/09/2026). Toujours citer la date.
