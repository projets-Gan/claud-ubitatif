---
id: immigration-ordres-quitter-eurostat-france-2024
type_fiche: fait
enonce: "Selon Eurostat (jeu migr_eiord, mise à jour du 30/09/2026), 128 740 ressortissants de pays tiers ont fait l'objet en France d'un ordre de quitter le territoire en 2024, le nombre le plus élevé de l'UE, devant l'Espagne (62 930) et l'Allemagne (57 075), pour un total UE de 464 820 (personnes, valeurs arrondies à 5)."
valeur: 128740
unite: "personnes (ressortissants de pays tiers)"
definition: "Statistique Eurostat « Third country nationals ordered to leave » : ressortissants de pays hors UE, EEE et Suisse, constatés en séjour irrégulier, faisant l'objet d'une décision administrative ou judiciaire leur imposant de quitter le territoire. Unité : personnes et non décisions ; transferts Dublin exclus ; données transmises par chaque État membre (pour la France, par le ministère de l'Intérieur à partir des saisies des préfectures)."
periode: "2024"
themes: [immigration]
sous_themes: [eloignements]
pays: [FR, UE, ES, DE]
biais_formulation: "1) Personnes ≠ OQTF : Eurostat compte des personnes ressortissantes de pays tiers, le ministère de l'Intérieur compte des mesures (129 833 « OQTF (et APRF) » en 2024 selon un rapport parlementaire, fait en attente immigration-oqtf-prononcees-ministere-2025) qui incluent aussi des ressortissants de l'UE et peuvent viser plusieurs fois la même personne. La quasi-égalité des deux nombres (écart de 0,8 %) n'est pas expliquée : ne pas la présenter comme une confirmation, ni comme la preuve que les deux séries mesurent la même chose. 2) Le classement reflète en partie la pratique administrative française, qui délivre largement des OQTF (notamment après un refus de titre de séjour ou le rejet d'une demande d'asile) ; il ne mesure pas le nombre de personnes en situation irrégulière et ne tient pas compte de la population des pays. 3) Un ordre de quitter le territoire n'indique pas si la personne est partie ou non. 4) Couverture de l'outre-mer non documentée dans les métadonnées françaises."
etat_donnee: provisoire
statut: valide
date_validite: 2027-05-31
date_ajout: 2026-11-02
date_derniere_verification: null
sources:
  - source: 2026-09-30-eurostat-ordres-quitter-territoire-migr-eiord
    extrait: "time=2024, citizen=TOTAL, age=TOTAL, sex=T, unit=PER : EU27_2020 : 464820 ; ES : 62930 ; DE : 57075 ; FR : 128740 (aucun autre pays déclarant au-dessus de 62930)"
    localisation: "API Eurostat, jeu migr_eiord, requête time=2024 tous pays (34 entrées géographiques), champ « updated » 2026-09-30"
contredit_par: []
notes: "Valide sur une source de niveau 1 (série statistique officielle d'Eurostat, méthode documentée dans 2024-02-21-eurostat-metadonnees-migr-eil-esms). Valeurs relues par le curateur le 2/11/2026 pour les 34 entrées (le classement complet a aussi été vérifié par le contradicteur). État « provisoire » par prudence : aucun indicateur de statut, mais les données Eurostat sont révisées (total UE 2025 révisé entre avril et septembre 2026). Les données françaises d'Eurostat ont la même origine administrative que celles du ministère de l'Intérieur (2026-03-23-eurostat-metadonnees-france-migr-eil-sims-fr). Date de validité : prochaine mise à jour annuelle attendue au printemps 2027 (date estimée)."
---

## Contexte

Série France (personnes) : 123 845 en 2019, 108 395 en 2020, 125 450 en 2021, 135 645 en
2022, 136 685 en 2023, 128 740 en 2024, 137 550 en 2025 (même jeu de données). Pour 2025,
voir immigration-ordres-quitter-eurostat-france-2025.

La part de la France dans le total UE 2024 est d'environ 27,7 % (calcul : 128 740 / 464 820,
non publié par Eurostat).

## Limites

Données révisables. Ne renseigne ni sur l'exécution des ordres de quitter, ni sur le
nombre de personnes en situation irrégulière. Pour comparer avec les retours effectifs,
voir immigration-eurostat-retours-ordres-methode : Eurostat avertit que les deux séries ne
se rapportent pas directement l'une à l'autre.
