---
id: immigration-retours-eurostat-france-2025
type_fiche: fait
enonce: "Selon Eurostat (jeu migr_eirtn, mise à jour du 25/09/2026), 14 940 ressortissants de pays tiers sont partis de France vers un pays tiers à la suite d'un ordre de quitter le territoire en 2025 (14 670 en 2024), et 18 930 toutes destinations confondues, y compris vers un autre État membre (16 665 en 2024). Pour les retours vers un pays tiers, la France est 2e de l'UE en 2025, derrière l'Allemagne (29 295) et devant la Suède (11 250)."
valeur: 14940
unite: "personnes (ressortissants de pays tiers renvoyés vers un pays tiers)"
definition: "Statistique Eurostat « Third country nationals returned following an order to leave » : ressortissants de pays tiers ayant effectivement quitté le territoire de l'État membre à la suite d'un ordre de quitter. Comprend les retours forcés et les retours volontaires aidés, et les retours volontaires non aidés lorsqu'ils sont enregistrés de façon fiable. Transferts Dublin exclus. Unité : personnes, arrondies à 5."
periode: "2025"
themes: [immigration]
sous_themes: [eloignements]
pays: [FR, UE, DE]
biais_formulation: "1) « Retours » au sens d'Eurostat ≠ « éloignements » du ministère de l'Intérieur : ces derniers incluent des ressortissants de l'UE et d'autres périmètres (24 985 éloignements en 2025 selon l'AFP d'après la DGEF, fait en attente immigration-eloignements-dgef-2025). 2) Les retours d'une année ne correspondent pas aux ordres de quitter de la même année : diviser 14 940 par 137 550 ne donne pas un « taux d'exécution » (avertissement d'Eurostat, voir immigration-eurostat-retours-ordres-methode). 3) Les départs spontanés non constatés ne sont pas comptés. 4) Classement en valeur absolue, sans rapport à la population ni au nombre d'ordres."
etat_donnee: provisoire
statut: valide
date_validite: 2027-05-31
date_ajout: 2026-11-02
date_derniere_verification: null
sources:
  - source: 2026-09-25-eurostat-retours-migr-eirtn
    extrait: "geo=FR : c_dest=THRD 2024 : 14670 ; 2025 : 14940 — c_dest=TOTAL 2024 : 16665 ; 2025 : 18930"
    localisation: "API Eurostat, jeu migr_eirtn, geo=FR, citizen=TOTAL, age=TOTAL, sex=T, 2023-2025 ; ordre des dimensions vérifié (id/size), champ « updated » 2026-09-25"
  - source: 2026-09-25-eurostat-retours-migr-eirtn
    extrait: "c_dest=THRD, time=2025 : EU27_2020 : 139270 ; DE : 29295 ; FR : 14940 ; SE : 11250 (aucun autre pays déclarant au-dessus de 11250)"
    localisation: "API Eurostat, jeu migr_eirtn, c_dest=THRD, time=2025, tous pays (34 entrées géographiques)"
contredit_par: []
notes: "Valide sur une source de niveau 1 (série statistique officielle d'Eurostat). Valeurs relues par le curateur le 2/11/2026 ; la correspondance des valeurs pour l'Allemagne, mise en doute par le chercheur, a été confirmée par le contradicteur puis par le curateur. Données révisables (Allemagne 2024 vers pays tiers : 15 230 dans le communiqué Eurostat de mai 2025, 18 695 au 25/09/2026). Date de validité estimée (mise à jour annuelle du printemps 2027)."
---

## Contexte

Allemagne : 18 695 retours vers un pays tiers en 2024 et 29 295 en 2025 ; 22 005 et 36 075
toutes destinations (même jeu). Total UE vers un pays tiers : 139 270 en 2025.

Calcul non publié par Eurostat, à ne pas présenter comme un taux : 14 940 / 137 550 ≈ 10,9 %
pour la France en 2025, 14 670 / 128 740 ≈ 11,4 % en 2024. La valeur 2024 coïncide avec le
« taux d'exécution » de 11,4 % donné par la commission des finances du Sénat d'après le
ministère de l'Intérieur : c'est une coïncidence de valeur, pas une corroboration (définitions
et sources différentes).

## Limites

Ne distingue pas retours forcés et volontaires : pour les retours forcés, voir
immigration-retours-forces-pays-tiers-eurostat-2025.
