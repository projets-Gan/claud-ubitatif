---
id: immigration-chomage-nes-hors-ue-eurostat-2025
type_fiche: fait
enonce: "En 2025, en France, le taux de chômage des personnes de 15 à 74 ans nées hors de l'Union européenne à 27 est de 13,1 %, contre 7,8 % pour les personnes nées dans un autre pays de l'UE, 7,0 % pour les personnes nées en France et 7,7 % pour l'ensemble (Eurostat, enquête sur les forces de travail, jeu lfsa_urgacob)."
valeur: 13.1
unite: "% de la population active"
definition: "Chômage au sens du BIT harmonisé par l'enquête sur les forces de travail de l'UE (volet français : enquête Emploi de l'INSEE), moyenne annuelle 2025. Classement par pays de naissance de la personne (dimension c_birth d'Eurostat), et non par statut d'immigré ni par nationalité. France entière, Mayotte incluse depuis 2024 selon la note méthodologique Eurostat. 15-74 ans, sexes réunis."
periode: "2025"
themes: [immigration, emploi]
sous_themes: [immigration-emploi, chomage]
pays: [FR]
biais_formulation: "1) « Né hors UE » ≠ « immigré extra-européen » ≠ « étranger » : la catégorie inclut des Français de naissance nés à l'étranger et classe selon l'UE à 27, non selon l'Europe géographique. 2) « Né en France » (7,0 %) inclut les descendants d'immigrés : ce n'est pas l'équivalent des « personnes sans ascendance migratoire » de l'INSEE (6,5 %, 15-64 ans) ni des « Français ». 3) Écart nés hors UE / nés en France : +6,1 points, rapport d'environ 1,9 (calcul du curateur sur valeurs arrondies, non publié par Eurostat). 4) Tranche d'âge 15-74 ans et champ incluant Mayotte : ne pas mélanger avec les tableaux INSEE (15-64 ans, hors Mayotte) ; la coïncidence du total (7,7 % dans les deux cas) est fortuite. 5) Rupture de série en 2024 : aucune évolution ne peut être tirée de la comparaison avec 2023 ou avant."
etat_donnee: definitif
statut: valide
date_validite: 2027-05-31
date_ajout: 2026-11-02
date_derniere_verification: null
sources:
  - source: 2026-10-30-eurostat-lfsa-urgacob-chomage-pays-naissance
    extrait: "Non-EU27 countries (from 2020) nor reporting country"
    localisation: "Jeu lfsa_urgacob, mise à jour du 2026-10-30, France (geo=FR), age=Y15-74, sex=T, unit=PC, année 2025 : valeur 13,1 (drapeau « d »). Même requête, 2025 : « EU27 countries (from 2020) except reporting country » 7,8 ; « Reporting country » 7,0 ; « Total » 7,7."
contredit_par: []
notes: "Validé par une seule source de niveau 1 (jeu de données statistique Eurostat). Valeurs 2025 confirmées par le contradicteur sur le JSON brut et relues par le curateur (2026-11-02) via l'API. État « definitif » : aucun drapeau « p » (provisoire) sur la valeur ; les données restent révisables lors des mises à jour du jeu. Drapeau « d » (« definition differs (see metadata) ») : selon la note employ_esms (lue via un outil de résumé), la France traite différemment depuis 2021 les personnes en chômage temporaire ; à confirmer par le relecteur. Date de validité : publication attendue des données annuelles 2026 (estimation, à ajuster)."
---

## Contexte

Le même jeu donne, pour 2025, 12,0 % pour l'ensemble des personnes nées à l'étranger.
Valeurs 2024 (rupture de série « bd ») : nés hors UE 12,3 % ; nés dans l'UE 7,3 % ; nés en
France 6,8 % ; total 7,4 %.

C'est la seule source du corpus qui distingue l'UE du reste du monde ; les tableaux de
l'INSEE (fait immigration-chomage-immigres-insee-2025) raisonnent par statut d'immigré et
par grande origine géographique, sans agrégat « hors UE ».

## Limites

- Estimation issue d'une enquête par sondage.
- Écart brut, non corrigé de l'âge, du diplôme ou de la catégorie sociale.
- Sens exact du drapeau « d » pour la France à confirmer dans les métadonnées.
