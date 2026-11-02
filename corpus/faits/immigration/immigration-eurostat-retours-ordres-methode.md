---
id: immigration-eurostat-retours-ordres-methode
type_fiche: fait
enonce: "Selon la méthodologie d'Eurostat, les statistiques d'ordres de quitter le territoire et de retours comptent des personnes et non des décisions, et une personne partie au cours d'une année peut avoir reçu son ordre de quitter une année antérieure : le nombre de personnes renvoyées au cours d'une période ne doit pas être directement rapporté au nombre de personnes ayant reçu un ordre de quitter au cours de la même période."
valeur: null
unite: null
definition: "Règles méthodologiques des statistiques européennes sur l'application de la législation sur l'immigration (migr_eil : migr_eiord, migr_eirtn, migr_eirtn1)."
periode: "2026"
themes: [immigration]
sous_themes: [eloignements]
pays: [UE, FR]
biais_formulation: "1) Un « taux d'exécution » obtenu en divisant les départs d'une année par les ordres ou les OQTF de la même année n'est pas un suivi des personnes : il ne dit pas quelle part des personnes visées est partie ou restée. Dire « X % des OQTF ne sont pas exécutées, donc 100 - X % des personnes visées restent en France » est une déduction que ces statistiques ne permettent pas (départs spontanés non constatés, OQTF multiples pour une même personne, OQTF annulées ou abrogées, départs l'année suivante). 2) Le ministère de l'Intérieur lui-même indique, selon un rapport parlementaire de 2026, que le rapprochement entre mesures exécutées et prononcées pose des difficultés « qui ne permettent pas valablement de calculer un taux d'exécution » (2026-09-16-assemblee-nationale-rapport-rodwell-immigration-irreguliere, partie I.C.1.a ; niveau 2, cité pour information). 3) Ce fait porte sur la méthode : il ne dit pas si l'exécution des OQTF est élevée ou faible."
etat_donnee: definitif
statut: valide
date_validite: 2027-11-02
date_ajout: 2026-11-02
date_derniere_verification: null
sources:
  - source: 2024-02-21-eurostat-metadonnees-migr-eil-esms
    extrait: "Each table refers to the number of persons, not to the number of administrative decisions or acts."
    localisation: "Métadonnées ESMS migr_eil, section 3.5 (Statistical unit)"
  - source: 2024-02-21-eurostat-metadonnees-migr-eil-esms
    extrait: "Persons who left the territory within the year may have been subject to an obligation to leave in a previous year."
    localisation: "Métadonnées ESMS migr_eil, section 3.4 (Statistical concepts and definitions)"
  - source: 2026-06-19-eurostat-retours-trimestriels-statistics-explained
    extrait: "… shall not be directly related to the number of persons ordered to leave in the same reference period."
    localisation: "Statistics Explained « Returns of irregular migrants - quarterly statistics », section « Data sources » (phrase commençant par « The number of persons returned in a given »)"
contredit_par: []
notes: "Valide sur des documents de niveau 1 du producteur de la statistique (métadonnées et publication méthodique d'Eurostat), conformément à la recommandation du contradicteur (constat méthodologique). Les deux documents émanent du même producteur : la validation repose sur la règle « une source de niveau 1 suffit », pas sur leur nombre. Période « 2026 » = année de consultation des règles méthodologiques ; date de validité fixée à un an faute de calendrier de révision des métadonnées. etat_donnee « definitif » renseigné parce que le validateur l'exige pour un fait validé par une source statistique unique : il s'agit ici de règles de méthode en vigueur à la date de consultation, pas d'une valeur chiffrée (à arbitrer par le relecteur)."
---

## Contexte

Ce fait sert à lire correctement les « taux d'exécution des OQTF » qui circulent (8,3 %,
« autour de 10 % », 11,4 %, « de l'ordre de 15 % », 4,5 %…) : ils rapportent un flux de
départs de l'année à un flux de mesures de la même année, avec des numérateurs et des
dénominateurs différents selon les auteurs. Voir immigration-taux-execution-oqtf-2024 et
immigration-taux-execution-oqtf-2025 (en attente).

## Limites

Les métadonnées ne portent que sur les statistiques Eurostat ; elles ne décrivent pas la
méthode des séries du ministère de l'Intérieur.
