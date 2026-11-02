---
# Modèle de rapport d'ANALYSE DE DOCUMENT. Copier ce fichier vers :
#   analyses/<id>.md
# Un rapport d'analyse n'est PAS une fiche du corpus : il ne sert jamais de preuve.
# Le document analysé (PDF) n'est jamais copié dans le dépôt.
id: auteur-titre-court-annee                 # identique au nom du fichier, ASCII, minuscules, tirets
type_fiche: analyse-document
document:
  titre: "Titre exact du document"
  auteur: "Prénom Nom"
  editeur: "Éditeur"
  date_publication: 2026-01-01               # ou seulement l'année : 2026
  isbn: null                                 # livre : ISBN ; sinon null
  url: null                                  # page de présentation officielle, si elle existe
  type_estime: analyse-essai                 # type de config/types-sources.yaml que ce document aurait s'il était une source
themes: [emploi]                              # codes de config/taxonomie.yaml
pays: [FR]
parties_analysees:                           # ce qui a été lu ; compléter au fil des analyses
  - partie: "Chapitre 1 — Titre"
    pages: "1-24"
    date_analyse: 2026-01-01
version_regles: 3                            # version de config/niveaux.yaml utilisée
---

## Résumé de l'analyse

Une ou deux phrases : nombre d'affirmations vérifiables relevées, répartition des verdicts,
part « non vérifiable avec le corpus actuel ». Pas de verdict global sur le document.

## Affirmations relevées

| n° | Page | Affirmation (reformulée) | Verdict | Faits du corpus utilisés |
|---|---|---|---|---|
| 1 | 12 | … | Non vérifiable avec le corpus actuel | — |
| 2 | 15 | … | Trompeur | [emploi-…](../corpus/faits/emploi/….md) |

Opinions, prévisions et jugements de valeur ignorés : N.

## Détail des verdicts (hors « non vérifiable »)

### Affirmation n : page P
**Verdict : …**

Explication, éléments manquants, biais de formulation et sources du corpus,
au format de réponse de l'agent vérificateur. Extrait du document : 15 mots maximum.

## Bilans

- Premier bilan : …
- Second bilan (subtilités, définitions, périodes) : …

## Recherches proposées

Affirmations non vérifiables, regroupées par sujet et classées du plus utile au moins utile.
Pour un document, aucune recherche n'est lancée automatiquement (`config/recherche.yaml`) :
l'utilisateur coche celles à lancer ; la colonne « Suivi » reçoit le lien de la Pull Request
de recherche. Une fois celle-ci fusionnée, relancer la vérification des affirmations concernées.

| Sujet | Affirmations | Thème (ou nouveau thème proposé) | Source primaire attendue | Suivi |
|---|---|---|---|---|
| … | 1, 4 | emploi | INSEE, enquête Emploi | — |

> Outil d'aide à la vérification fondé sur un corpus limité ; il ne remplace pas un travail journalistique.
