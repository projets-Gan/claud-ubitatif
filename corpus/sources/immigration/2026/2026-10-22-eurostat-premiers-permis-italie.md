---
id: 2026-10-22-eurostat-premiers-permis-italie
type_fiche: source
titre: "First permits by reason, length of validity and citizenship (migr_resfirst) – Italie"
editeur: "Eurostat"
auteurs: []
type: donnees-officielles
url: "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/migr_resfirst?geo=IT&duration=TOTAL&citizen=TOTAL&lang=EN&sinceTimePeriod=2010"
archive: null
hash_sha256: null
date_publication: 2026-10-22
date_consultation: 2026-11-02
themes: [immigration]
sous_themes: [titres-de-sejour]
pays: [IT]
langue: en
depend_de: []
notes: >
  Extraction de l'API Eurostat (JSON-stat), série Italie 2010-2025, duration=TOTAL,
  citizen=TOTAL, unité personnes. « updated » : 2026-10-22. Drapeau « b » (rupture de
  série) sur TOTAL et OTH en 2022 ; aucun drapeau sur 2023-2025. Annexe qualité Italie
  consultée le 2/11/2026 :
  https://ec.europa.eu/eurostat/cache/metadata/Annexes/migr_res_esqrs_it_an_1.pdf
  (politique de révision non renseignée). Archive impossible (archive.org inaccessible) ;
  empreinte non calculée.
---

## Résumé

Série Eurostat des premiers titres de séjour délivrés par l'Italie à des ressortissants de
pays tiers, par motif (famille, études, emploi, autres), 2010-2025. Les données sont
transmises par l'Italie selon sa législation nationale.

## Extraits

> Valeurs (personnes), reason=TOTAL / FAM / EDUC / EMP / OTH :
> 2024 : 346411 / 110093 / 20679 / 39090 / 176549
> 2025 : 433099 / 176876 / 36358 / 57362 / 162503
> (API migr_resfirst, geo=IT, duration=TOTAL, citizen=TOTAL, unit=PER)

> Série emploi (EMP) / total, années choisies : 2010 359051 / 589988 ; 2015 17370 / 178884 ;
> 2021 50597 / 274095 ; 2022 66791 / 337788 ; 2023 38103 / 389542.

> « Italy doesn't count pupils and au pairs. » (annexe qualité Italie, section 4.2)

## Points d'attention

- Rupture de série en 2022 (drapeau « b » sur le total et sur « Other ») : prudence pour les
  comparaisons de part avant et après 2022.
- Champ national différent de la France (élèves et au pair non comptés). La section 8 de
  l'annexe écrit « Italy doesn't count students, volunteers, pupils and au pairs », ce qui
  paraît contredire l'existence de valeurs EDUC : ambiguïté à signaler, non résolue.
- Politique de révision non documentée par l'Italie : l'état provisoire ou définitif de 2024
  et 2025 n'est pas connu.
- Les permis italiens pour emploi dépendent de quotas annuels ; aucune conclusion sur les
  politiques nationales ne peut être tirée de cette série seule.
