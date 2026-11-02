---
id: 2026-10-30-eurostat-lfsa-urganedm-chomage-statut-migratoire
type_fiche: source
titre: "Unemployment rates by sex, age, migration status, citizenship and educational attainment level [lfsa_urganedm]"
editeur: "Eurostat"
auteurs: []
type: donnees-officielles
url: "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_urganedm?geo=FR&age=Y15-74&sex=T&isced11=TOTAL&citizen=TOTAL&sinceTimePeriod=2021&lang=EN"
archive: null
hash_sha256: null
date_publication: 2026-10-30
date_consultation: 2026-11-02
themes: [immigration, emploi]
sous_themes: [immigration-emploi, chomage]
pays: [FR, UE]
langue: en
depend_de: []
notes: >
  Jeu de données EFT-UE (volet français : enquête Emploi de l'INSEE), traitement Eurostat.
  Date de publication = date de dernière mise à jour du jeu (« updated » :
  2026-10-30T23:00:00+0100). URL = requête de l'API de diffusion effectivement lue (page du Data Browser non consultée) (geo=FR, age=Y15-74,
  sex=T, isced11=TOTAL, citizen=TOTAL) :
  https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_urganedm?geo=FR&age=Y15-74&sex=T&isced11=TOTAL&citizen=TOTAL&sinceTimePeriod=2021&lang=EN
  Lecture concordante par le chercheur, le contradicteur (JSON brut) et le curateur.
  Archive non créée et hash non calculé (accès réseau du shell refusé pour ec.europa.eu).
---

## Résumé

Taux de chômage annuels (BIT, harmonisés EFT-UE) selon le statut migratoire défini par
le pays de naissance de la personne et de ses parents : nés dans le pays de deux parents
nés dans le pays, « seconde génération » (nés dans le pays d'au moins un parent né à
l'étranger, avec le détail un parent / deux parents), « première génération » (nés à
l'étranger), statut inconnu. France, 15-74 ans, tous niveaux d'éducation, toutes
nationalités.

## Extraits

Valeurs France, 15-74 ans, en %, 2025 (drapeau « d » pour toutes) :

- « Native-born with both parents native-born » : 6,3
- « Native-born with one or both parents born abroad (second generation) » : 10,1
- « Native-born with one parent born abroad (second generation) » : 8,4
- « Native-born with both parents born abroad (second generation) » : 12,3
- « Foreign-born (first generation) » : 12,0
- « Native-born » : 6,9 ; « Unknown » : 11,6 ; « Total » : 7,7

Seconde génération, 2021 à 2025 : 9,1 (bd) / 8,1 (d) / 8,1 (d) / 10,1 (bd) / 10,1 (d) ;
« Unknown » : 19,4 / 19,4 / 19,2 / 9,9 / 11,6.

## Points d'attention

- « Parent né à l'étranger » ≠ « parent immigré » au sens de l'INSEE : un parent français
  de naissance né à l'étranger est compté ici. La « seconde génération » Eurostat n'est donc
  pas l'équivalent des « descendants d'immigrés » de l'INSEE.
- Ruptures de série (« bd ») en 2021 et 2024. La chute de la catégorie « Unknown » (19,2 %
  en 2023, 9,9 % en 2024) et le saut de la seconde génération (8,1 % → 10,1 %) suggèrent un
  changement de classement : aucune évolution ne doit être tirée de part et d'autre de 2024.
- Mayotte incluse à partir de 2024 (note `employ_esms`, lue via un outil de résumé).
- « Native-born » vaut 6,9 ici, contre 7,0 pour « Reporting country » dans lfsa_urgacob
  (2025) : traitements propres à chaque jeu ; ne pas mélanger les deux tableaux.
