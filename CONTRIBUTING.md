# Contribuer

Merci de votre intérêt. Toute contribution passe par GitHub et est relue par un humain.

## Proposer une source sans toucher au code

Ouvrez une **Issue** avec le modèle « Proposer une source » : lien, éditeur, date, fait(s) que la source permet d'établir. Un mainteneur (ou l'agent Curateur) préparera les fiches.

## Ajouter ou modifier des fiches

1. Faites un *fork* du dépôt (ou créez une branche si vous êtes mainteneur). Ne travaillez jamais directement sur `main`.
2. Installez les dépendances une fois : `python -m pip install -r requirements.txt`.
3. Copiez `modeles/source.md` ou `modeles/fait.md` au bon endroit :
   - sources : `corpus/sources/<premier-theme>/<annee-de-publication>/<id>.md`
   - faits : `corpus/faits/<premier-theme>/<id>.md`
   - le nom du fichier est l'`id` : ASCII, minuscules, chiffres et tirets (ex. `2026-10-15-insee-chomage-t3.md`).
4. Utilisez uniquement les valeurs de `config/taxonomie.yaml` et `config/types-sources.yaml`. Pour un nouveau thème ou pays, modifiez d'abord la configuration dans une PR séparée.
5. Lancez :
   ```
   python scripts/valider_corpus.py
   python scripts/generer_index.py
   ```
   Corrigez toutes les erreurs. Les avertissements (archive manquante, date de validité dépassée) sont à traiter quand c'est possible.
6. Ouvrez une **Pull Request** en remplissant le modèle : justification de l'indépendance des sources, statut des faits.

Avec Claude Code, vous pouvez demander : « Utilise l'agent curateur pour ajouter cette source : <lien> ». Il suit les mêmes étapes.

## Règles de relecture

Une PR est fusionnée si :
- la validation automatique passe ;
- chaque fait `valide` repose sur au moins deux sources réellement indépendantes ;
- les extraits sont courts, exacts et localisés ;
- les définitions et périmètres sont explicites ;
- rien n'est copié au-delà du droit de courte citation.

## Licences

En contribuant, vous acceptez que votre contribution soit publiée sous Apache-2.0 pour le code et sous Licence Ouverte 2.0 pour le contenu du corpus (voir `LICENSE` et `LICENSE-CONTENU`).

## Signaler une erreur

Ouvrez une Issue en citant la fiche concernée (son `id`) et la source qui la contredit.
