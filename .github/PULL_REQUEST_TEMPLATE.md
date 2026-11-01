## Objet

<!-- Que change cette Pull Request ? (nouvelles sources, nouveaux faits, mise à jour, configuration, code) -->

## Fiches ajoutées ou modifiées

| Fiche (id) | Type | Statut | Sources utilisées |
|---|---|---|---|
|  | source / fait | valide / en-attente / conteste |  |

## Justification des faits « valide »

<!-- Pour chaque fait « valide », préciser la voie de validation :
     - 1 source de niveau 0 ou 1 : pourquoi le document est-il primaire et non orienté ? Localisation de l'extrait, état provisoire / définitif.
     - 2 sources de niveau 2 ou mieux : pourquoi sont-elles indépendantes ? (éditeurs différents, pas de reprise d'un même communiqué ou d'une même dépêche) -->

## Avis du contradicteur

<!-- Résumé de l'avis de l'agent contradicteur et traitement de chaque objection (retenue, écartée et pourquoi). -->

## Points d'attention pour le relecteur

<!-- Faits validés par une seule source (à relire en priorité), biais de formulation, archive manquante, extrait à confirmer, définition ambiguë, sujet sensible… -->

## Vérifications

- [ ] `python scripts/valider_corpus.py` passe sans erreur
- [ ] `python scripts/generer_index.py` a été lancé et l'index est commité
- [ ] Les extraits sont courts, exacts et localisés (pas d'article complet)
- [ ] Les définitions et périmètres sont explicites
- [ ] Aucun secret (clé API, jeton) n'est présent
