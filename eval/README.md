# Jeu d'évaluation

Ce dossier contiendra 50 à 100 affirmations dont le verdict est connu, issues de vérifications déjà publiées (AFP Factuel, Les Décodeurs, CheckNews…). Elles servent à mesurer, à chaque évolution des agents ou du corpus :

- le **taux de verdicts corrects** ;
- le **taux de citations incorrectes** (extrait absent du corpus ou mal attribué) ;
- la part de « non vérifiable » (qui doit baisser à mesure que le corpus grandit, sans être remplacée par des erreurs).

Les affirmations sont listées dans `affirmations.yaml`, au format :

```yaml
- id: eval-001                       # identifiant unique
  affirmation: "Texte exact de l'affirmation testée"
  theme: emploi                       # code de config/taxonomie.yaml
  verdict_attendu: trompeur           # code de config/verdicts.yaml
  justification: "Résumé du fact-check de référence, avec vos propres mots"
  reference: "https://…"              # lien vers le fact-check publié
  date_reference: 2026-01-01
```

Le jeu d'évaluation sera constitué lors de l'étape dédiée (voir le tableau Trello du projet).
