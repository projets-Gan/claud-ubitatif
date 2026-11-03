---
id: 2026-10-22-eurostat-premiers-permis-france
type_fiche: source
titre: "First permits by reason, length of validity and citizenship (migr_resfirst) – France"
editeur: "Eurostat"
auteurs: []
type: donnees-officielles
url: "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/migr_resfirst?geo=FR&duration=TOTAL&citizen=TOTAL&lang=EN&sinceTimePeriod=2010"
archive: null
hash_sha256: null
date_publication: 2026-10-22
date_consultation: 2026-11-02
themes: [immigration]
sous_themes: [titres-de-sejour]
pays: [FR]
langue: en
depend_de: []
notes: >
  Extraction de l'API Eurostat (JSON-stat), série France 2010-2025, toutes durées de
  validité (duration=TOTAL), toutes nationalités (citizen=TOTAL), unité personnes (PER).
  Date de publication = date de mise à jour des données indiquée par l'API
  (« updated » : 2026-10-22). Aucun drapeau (« status ») dans la réponse pour la France.
  Valeurs relues par le chercheur, le contradicteur et le curateur (2/11/2026) au moyen
  d'un outil de lecture qui restitue les valeurs du fichier ; une relecture dans le
  visualiseur Eurostat reste conseillée. Données transmises par le ministère de
  l'Intérieur (base AGDREF), d'après le rapport qualité France d'Eurostat
  (https://ec.europa.eu/eurostat/cache/metadata/EN/migr_res_esqrs_fr.htm, consulté le
  2/11/2026). Archive impossible (archive.org inaccessible depuis l'environnement de
  travail) ; empreinte non calculée (téléchargement direct refusé par le proxy).
---

## Résumé

Série statistique d'Eurostat sur les premiers titres de séjour (« first permits »)
délivrés par la France à des ressortissants de pays tiers, ventilés selon quatre motifs :
famille (FAM), études (EDUC), emploi (EMP) et autres (OTH, qui regroupe notamment la
protection internationale, les motifs humanitaires et des motifs divers). Les données
sont transmises par le ministère de l'Intérieur à partir de la base AGDREF.

## Extraits

> Valeurs (personnes), reason=TOTAL / FAM / EDUC / EMP / OTH :
> 2023 : 338877 / 92719 / 112399 / 58762 / 74997
> 2024 : 345587 / 91030 / 112594 / 58603 / 83360
> 2025 : 377462 / 90959 / 118404 / 50848 / 117251
> (API migr_resfirst, geo=FR, duration=TOTAL, citizen=TOTAL, unit=PER, « updated » 2026-10-22T23:00:00+0200)

> « Preliminary data published in July n + 1 » ; « Final data published in January n + 2 »
> (rapport qualité France, section 6.5 « Data revision - policy »)

> « There is no significant difference the data provided to Eurostat and the data published at national level. »
> (rapport qualité France, section 5.1.2)

## Points d'attention

- Nomenclature Eurostat différente de celle de la DGEF : « Other » regroupe l'humanitaire et
  les « divers » de la DGEF ; l'emploi Eurostat n'est pas exactement le motif « économique »
  de la DGEF. Ne pas mélanger les deux séries dans un même calcul.
- État : d'après la politique de révision nationale, 2025 est provisoire (données
  préliminaires de juillet N+1) et 2024 définitif (janvier N+2). L'absence de drapeau « p »
  dans l'API ne prouve rien à elle seule.
- Champ des mineurs non établi : le rapport qualité France mentionne une catégorie
  « Children (Minor/ Adult) » (famille) et « Foreign minor entry » parmi les autres motifs
  (section 8.1). On ne peut pas affirmer que la série Eurostat exclut les mineurs comme la
  série DGEF.
- Les critères détaillés d'un « first permit » (durée minimale de validité, délai entre deux
  titres) figurent dans les métadonnées migr_res_esms, qui n'ont pas pu être lues.
