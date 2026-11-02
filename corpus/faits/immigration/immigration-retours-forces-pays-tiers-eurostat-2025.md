---
id: immigration-retours-forces-pays-tiers-eurostat-2025
type_fiche: fait
enonce: "Selon Eurostat (jeu trimestriel migr_eirtn1, mise à jour du 30/09/2026), pour les retours forcés de ressortissants de pays tiers vers un pays tiers, la France est au 2e rang de l'UE à chacun des quatre trimestres de 2025 (1 700, 1 555, 1 435 et 1 495 personnes), derrière l'Allemagne (3 625, 3 445, 3 710 et 3 370) et devant l'Italie (1 245, 1 150, 1 110 et 1 270)."
valeur: null
unite: "personnes par trimestre"
definition: "Statistique Eurostat des ressortissants de pays tiers renvoyés à la suite d'un ordre de quitter le territoire, type de retour « forcé » (enforced return : une procédure d'exécution a été engagée), destination « pays tiers » (hors États membres). Données trimestrielles, personnes, arrondies à 5."
periode: "2025"
themes: [immigration]
sous_themes: [eloignements]
pays: [FR, UE, DE, IT]
biais_formulation: "1) Déclaration du ministre de l'Intérieur rapportée par Public Sénat le 28/01/2026 (2026-01-28-public-senat-nunez-reconduites-forcees) : « En Europe, nous sommes, avec l'Allemagne, le pays qui reconduit le plus de manière forcée vers les pays tiers ». Le rang de la France (2e) est conforme aux données ; mais la France en effectue à chaque trimestre moins de la moitié de l'Allemagne, ce que l'expression « avec l'Allemagne » ne dit pas. Le titre de l'article (« Nous sommes le pays, en Europe, qui reconduit le plus… ») supprime « avec l'Allemagne » et ne correspond pas aux données. 2) « Retour forcé » au sens d'Eurostat (ressortissants de pays tiers, vers un pays tiers) ≠ « éloignement forcé » du ministère de l'Intérieur (15 569 en 2025 selon l'AFP d'après la DGEF), qui couvre un périmètre plus large (ressortissants de l'UE, destinations dans l'UE). 3) Valeurs absolues, sans rapport à la population ni au nombre d'ordres de quitter."
etat_donnee: provisoire
statut: valide
date_validite: 2026-12-31
date_ajout: 2026-11-02
date_derniere_verification: null
sources:
  - source: 2026-09-30-eurostat-retours-par-type-migr-eirtn1
    extrait: "return=FORC, c_dest=THRD — FR : 2025-Q1 1700, Q2 1555, Q3 1435, Q4 1495 ; DE : 3625, 3445, 3710, 3370 ; IT : 1245, 1150, 1110, 1270"
    localisation: "API Eurostat, jeu migr_eirtn1, citizen=TOTAL, age=TOTAL, sex=T, c_dest=THRD, return=FORC, une requête par trimestre de 2025, tous pays ; champ « updated » 2026-09-30"
contredit_par: []
notes: "Valide sur une source de niveau 1 (série statistique officielle d'Eurostat). Le classement repose sur les valeurs publiées de chaque trimestre (vérifiées par le curateur le 2/11/2026 pour tous les pays déclarants), et non sur une somme. Ce fait lève l'objection bloquante n° 1 du contradicteur (déclaration ministérielle jugée « non établie » par le chercheur faute de données de ventilation). Le jeu annuel migr_eirt_vol est vide pour la France et l'Allemagne de 2023 à 2025 selon le contradicteur. Date de validité : prochaine mise à jour trimestrielle attendue vers la fin 2026 (date estimée), qui peut réviser 2025."
---

## Contexte

Calculs non publiés par Eurostat (sommes de trimestres arrondis, susceptibles de différer
d'une donnée annuelle) : environ 6 185 retours forcés vers un pays tiers pour la France en
2025, 14 150 pour l'Allemagne, 4 775 pour l'Italie, 53 860 pour l'UE.

Un rapport parlementaire de septembre 2026 (2026-09-16-assemblee-nationale-rapport-rodwell-immigration-irreguliere)
compte, d'après la police aux frontières, 6 161 éloignements forcés vers un pays tiers
en 2025, valeur proche de la somme ci-dessus : même origine administrative, ce n'est pas une
confirmation indépendante.

## Limites

Données trimestrielles révisables. Le T1 et le T2 2026 sont disponibles dans le même jeu
(non repris ici).
