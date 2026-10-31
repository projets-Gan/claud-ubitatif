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

Avec Claude Code, vous pouvez demander : « Ajoute au corpus cette source : <lien> ». Claude Code enchaîne alors les agents chercheur-sources, contradicteur et curateur, qui suivent les mêmes étapes.

## Faire évoluer les règles

Les niveaux de fiabilité et les règles de validation sont dans `config/niveaux.yaml`. Toute proposition de changement passe par une Pull Request qui met à jour ce fichier (version, date, historique) et la section « Évolution de la méthode » de `METHODOLOGIE.md`. Le classement d'une source au niveau 4 (`config/sources-niveau-4.yaml`) exige des critères publics et au moins deux preuves.

## Règles de relecture

Une PR est fusionnée si :
- la validation automatique passe ;
- chaque fait `valide` respecte `config/niveaux.yaml` : 1 source de niveau 0 ou 1 (avec localisation précise de l'extrait et, pour une statistique, son état provisoire ou définitif), ou 2 sources de niveau 2 ou mieux réellement indépendantes ;
- les biais de formulation sont signalés (champ `biais_formulation`) ;
- chaque source est classée selon le document lui-même, pas selon l'organisme qui le publie (un communiqué de ministère est de niveau 2, son tableau statistique de niveau 1) ;
- les extraits sont courts, exacts et localisés ;
- les définitions et périmètres sont explicites ;
- rien n'est copié au-delà du droit de courte citation.

## Licences

En contribuant, vous acceptez que votre contribution soit publiée sous Apache-2.0 pour le code et sous Licence Ouverte 2.0 pour le contenu du corpus (voir `LICENSE` et `LICENSE-CONTENU`).

## Signaler une erreur

Ouvrez une Issue en citant la fiche concernée (son `id`) et la source qui la contredit.
