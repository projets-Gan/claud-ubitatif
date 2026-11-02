---
id: 2026-10-30-eurostat-lfsa-urgacob-chomage-pays-naissance
type_fiche: source
titre: "Unemployment rates by sex, age and country of birth (%) [lfsa_urgacob]"
editeur: "Eurostat"
auteurs: []
type: donnees-officielles
url: "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_urgacob?geo=FR&age=Y15-74&sex=T&unit=PC&sinceTimePeriod=2023&lang=EN"
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
  Jeu de données de l'enquête sur les forces de travail de l'UE (EFT-UE), dont le volet
  français est l'enquête Emploi de l'INSEE : même enquête d'origine que la source
  2026-06-22-insee-chomage-immigres-descendants-2025, mais traitement et définitions
  propres à Eurostat (pas une reprise de la publication INSEE). Date de publication = date
  de dernière mise à jour du jeu (champ « updated » : 2026-10-30T23:00:00+0100). URL = requête de l'API de diffusion
  effectivement lue (page du Data Browser non consultée) (filtre geo=FR, age=Y15-74, sex=T, unit=PC) :
  https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsa_urgacob?geo=FR&age=Y15-74&sex=T&unit=PC&sinceTimePeriod=2023&lang=EN
  Lecture concordante par le chercheur, le contradicteur (JSON brut) et le curateur.
  Archive non créée et hash non calculé (accès réseau du shell refusé pour ec.europa.eu ;
  le contenu de l'API évolue à chaque mise à jour).
---

## Résumé

Taux de chômage annuels (au sens du BIT, harmonisés EFT-UE) par sexe, âge et pays de
naissance, pour chaque pays de l'UE. Pour la France, 15-74 ans, sexes réunis, la série
distingue les personnes nées dans le pays, nées dans un autre pays de l'UE à 27, nées
hors de l'UE à 27, nées à l'étranger (ensemble) et le total.

## Extraits

Valeurs France, 15-74 ans, sexes réunis, en % (2023 / 2024 / 2025), avec les libellés
de catégorie de la dimension `c_birth` :

- « Non-EU27 countries (from 2020) nor reporting country » : 12,5 / 12,3 / 13,1
- « EU27 countries (from 2020) except reporting country » : 5,9 / 7,3 / 7,8
- « Foreign country » : 10,9 / 11,2 / 12,0
- « Reporting country » : 6,8 / 6,8 / 7,0
- « Total » : 7,3 / 7,4 / 7,7

Drapeaux : « d » en 2023 et 2025 ; « bd » en 2024. Libellés Eurostat : « d » = « definition differs (see metadata) » ; « bd » = « break in time series, definition differs (see metadata) ».

## Points d'attention

- Classement par **pays de naissance**, pas par statut d'immigré au sens de l'INSEE ni par
  nationalité : « né hors UE » inclut des Français de naissance nés à l'étranger et exclut
  les immigrés nés dans l'UE ; « né en France » inclut les descendants d'immigrés.
- Drapeau « d » : selon la note méthodologique Eurostat `employ_esms` (lue via un outil de
  résumé, à confirmer), la France continue depuis 2021 de traiter différemment les
  personnes en chômage temporaire (test du lien à l'emploi), ce qui expliquerait le drapeau.
  Rupture « bd » en 2024 : la même note indique l'inclusion de Mayotte à partir de 2024.
  Aucune évolution ne doit être tirée de part et d'autre de 2024.
- Le champ Eurostat 2025 inclut donc Mayotte, contrairement aux tableaux INSEE « France
  hors Mayotte ».
- Pas de drapeau « p » (provisoire) sur les valeurs citées ; données révisables lors des
  mises à jour du jeu.
