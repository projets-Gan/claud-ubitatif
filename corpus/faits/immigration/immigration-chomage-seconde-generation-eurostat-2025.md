---
id: immigration-chomage-seconde-generation-eurostat-2025
type_fiche: fait
enonce: "En 2025, en France, le taux de chômage des personnes de 15 à 74 ans nées en France d'au moins un parent né à l'étranger (« seconde génération » au sens d'Eurostat) est de 10,1 %, contre 6,3 % pour les personnes nées en France de deux parents nés en France (Eurostat, jeu lfsa_urganedm)."
valeur: 10.1
unite: "% de la population active"
definition: "Chômage au sens du BIT harmonisé par l'enquête sur les forces de travail de l'UE (volet français : enquête Emploi de l'INSEE), moyenne annuelle 2025, 15-74 ans, tous niveaux d'éducation, toutes nationalités. Statut migratoire Eurostat défini par le pays de naissance de la personne et de ses parents (et non par le statut d'immigré des parents au sens de l'INSEE). Mayotte incluse depuis 2024 selon la note méthodologique Eurostat."
periode: "2025"
themes: [immigration, emploi]
sous_themes: [immigration-emploi, chomage]
pays: [FR]
biais_formulation: "1) « Parent né à l'étranger » ≠ « parent immigré » : un parent français de naissance né à l'étranger compte ici. La « seconde génération » Eurostat (10,1 %, 15-74 ans) n'est donc pas comparable terme à terme aux « descendants d'immigrés » de l'INSEE (11,7 %, 15-64 ans, hors Mayotte). 2) Écart : +3,8 points, rapport d'environ 1,6 (calcul du curateur sur valeurs arrondies, non publié par Eurostat). 3) Détail : 8,4 % avec un seul parent né à l'étranger, 12,3 % avec deux parents nés à l'étranger. 4) Ruptures de série en 2021 et en 2024 : la seconde génération passe de 8,1 % (2023) à 10,1 % (2024) au moment où la part de statut « inconnu » baisse fortement ; aucune évolution ne peut être tirée de part et d'autre de 2024. 5) La catégorie « Unknown » (11,6 % de chômage en 2025, effectif non connu) n'est pas négligeable. 6) Ne pas mélanger avec le jeu lfsa_urgacob : « Native-born » vaut ici 6,9 %, contre 7,0 % pour « Reporting country » dans lfsa_urgacob."
etat_donnee: definitif
statut: valide
date_validite: 2027-05-31
date_ajout: 2026-11-02
date_derniere_verification: null
sources:
  - source: 2026-10-30-eurostat-lfsa-urganedm-chomage-statut-migratoire
    extrait: "Native-born with one or both parents born abroad (second generation)"
    localisation: "Jeu lfsa_urganedm, mise à jour du 2026-10-30, France (geo=FR), age=Y15-74, sex=T, isced11=TOTAL, citizen=TOTAL, année 2025 : valeur 10,1 (drapeau « d »). Même requête, 2025 : « Native-born with both parents native-born » 6,3."
contredit_par: []
notes: "Validé par une seule source de niveau 1 (jeu de données statistique Eurostat). Valeurs 2025 confirmées par le contradicteur sur le JSON brut et relues par le curateur via l'API. État « definitif » : aucun drapeau « p » ; données révisables lors des mises à jour du jeu. Drapeau « d » à confirmer dans les métadonnées (voir la fiche source)."
---

## Contexte

Valeurs 2025 du même jeu : nés à l'étranger (« first generation ») 12,0 % ; nés en France
(ensemble) 6,9 % ; total 7,7 %. Pour la définition de l'INSEE (descendants d'immigrés),
voir immigration-chomage-descendants-immigres-insee-2025.

## Limites

- Estimation issue d'une enquête par sondage.
- Écart brut, non corrigé de l'âge, du diplôme ou de la catégorie sociale ; le corpus ne
  contient pas encore de mesure à caractéristiques comparables.
