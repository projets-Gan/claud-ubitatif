---
id: immigration-premiers-permis-eurostat-france-2024
type_fiche: fait
enonce: "Selon Eurostat (série migr_resfirst, données mises à jour le 22 octobre 2026), la France a délivré 345 587 premiers titres de séjour à des ressortissants de pays tiers en 2024 : 112 594 pour études, 91 030 pour motifs familiaux, 58 603 pour emploi et 83 360 pour autres motifs (dont la protection internationale et les motifs humanitaires)."
valeur: 345587
unite: "premiers titres de séjour (personnes)"
definition: "Premiers titres de séjour (« first permits ») au sens d'Eurostat, toutes durées de validité et toutes nationalités de pays tiers, ventilés en quatre motifs (famille, études, emploi, autres). Données transmises par le ministère de l'Intérieur (base AGDREF). Les critères détaillés d'Eurostat (durée minimale de validité, délai entre deux titres) n'ont pas été lus."
periode: "2024"
themes: [immigration]
sous_themes: [titres-de-sejour]
pays: [FR]
biais_formulation: "1) Un premier titre n'est pas une arrivée : il peut être délivré à une personne déjà présente (régularisation, protection accordée à un demandeur d'asile entré une année antérieure). 2) Les motifs Eurostat ne sont pas ceux de la DGEF : « autres » regroupe l'humanitaire et les « divers » de la DGEF ; ne pas mélanger les deux nomenclatures dans un même calcul. 3) Le motif est le motif administratif du titre, pas la motivation de la personne : ces données ne disent rien de l'attrait des prestations sociales ni de l'activité réelle des titulaires (un titulaire d'un titre familial ou étudiant peut travailler). 4) Champ des mineurs non établi pour la série Eurostat (le rapport qualité France mentionne des catégories « Children (Minor/ Adult) » et « Foreign minor entry »), alors que la série DGEF ne compte que les majeurs. 5) Les citoyens de l'UE, de l'EEE et de la Suisse n'ont pas de titre et ne sont pas comptés."
etat_donnee: definitif
statut: valide
date_validite: 2027-09-30
date_ajout: 2026-11-02
date_derniere_verification: null
sources:
  - source: 2026-10-22-eurostat-premiers-permis-france
    extrait: "2024 : TOTAL 345587 ; FAM 91030 ; EDUC 112594 ; EMP 58603 ; OTH 83360 (personnes)"
    localisation: "API Eurostat migr_resfirst, geo=FR, time=2024, reason=TOTAL/FAM/EDUC/EMP/OTH, duration=TOTAL, citizen=TOTAL, unit=PER, mise à jour du 2026-10-22 ; aucun drapeau"
contredit_par: []
notes: "Validé par une seule source de niveau 1 (série statistique Eurostat, document primaire non commenté). État définitif : selon le rapport qualité France d'Eurostat (section 6.5), les données définitives sont publiées en janvier N+2, soit janvier 2026 pour 2024 ; le total est par ailleurs identique au chiffre DGEF 2024 (345 587) repris par la presse. Date de validité : prochaine diffusion annuelle Eurostat (estimée à l'automne 2027), qui pourrait réviser la série."
---

## Contexte

En 2024, les études sont le premier motif des premiers titres délivrés par la France
(environ un tiers, par calcul), devant la famille, les autres motifs et l'emploi. À
rapprocher des 313 000 entrées d'immigrés estimées par l'INSEE pour la même année
(fait `immigration-entrees-immigres-insee-2024`), qui ne mesurent pas la même chose.

## Limites

Les parts éventuellement citées sont des calculs à partir de ces valeurs, pas des chiffres
publiés par Eurostat. Les définitions détaillées d'Eurostat (métadonnées migr_res_esms)
n'ont pas pu être lues.
