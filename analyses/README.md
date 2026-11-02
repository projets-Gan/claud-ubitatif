# Analyses de documents

Ce dossier contient les rapports produits par l'agent **vérificateur** en mode « analyse de document » : un livre, un rapport ou une tribune (souvent un PDF) est lu chapitre par chapitre, ses affirmations vérifiables sont relevées et comparées au corpus.

## Règles

- **Le document analysé n'est jamais copié dans le dépôt.** Il reste sur le poste de l'utilisateur ; seul le rapport est versionné. Les fichiers PDF sont ignorés par Git et la validation automatique refuse tout PDF versionné.
- **Un rapport d'analyse n'est pas une fiche du corpus.** Les affirmations qu'il contient sont ce qu'on vérifie, jamais ce qui prouve : le vérificateur ne s'appuie jamais sur ce dossier pour rendre un verdict.
- **Droit d'auteur** : affirmations reformulées, numéro de page, et au plus un extrait de 15 mots par affirmation.
- **Pas de verdict global** sur le document ni sur son auteur : des verdicts par affirmation uniquement.
- Chaque rapport indique la **version des règles** utilisée. Quand le corpus a grandi, les affirmations « non vérifiables » peuvent être relancées et le rapport mis à jour par Pull Request.

## Utilisation

Dans Claude Code, par exemple :

> Analyse le chapitre 3 (pages 45 à 70) du PDF `C:\Users\…\livre.pdf`

Le rapport suit le modèle `modeles/analyse-document.md` et s'appelle `analyses/<auteur>-<titre-court>-<annee>.md`.
