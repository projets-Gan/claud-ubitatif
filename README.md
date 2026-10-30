# claud-ubitatif

Agents d'aide à la vérification de l'actualité économique et politique française, fondés sur un corpus de sources public et vérifié.

> **Outil d'aide à la vérification, pas un arbitre.** Les verdicts dépendent d'un corpus limité ; ils ne remplacent pas un travail journalistique.

## Principe

- **Agent Vérificateur** : vous lui soumettez une information ; il indique, affirmation par affirmation, si elle est *exacte*, *fausse*, *trompeuse*, *incomplète* ou *non vérifiable*, en citant uniquement les fiches du corpus.
- **Agent Curateur** : il aide à enrichir le corpus. Un fait n'est validé que s'il repose sur **une source primaire officielle** (statistique ou texte juridique) ou sur **deux sources indépendantes** fiables.
- **Corpus public** : fiches Markdown (sources et faits) relues par des humains via Pull Request.

Thèmes de départ : **immigration**, **emploi**, **finances publiques**. Sources principalement françaises (INSEE, DARES, Eurostat, Légifrance, Cour des comptes, AFP, presse de référence…).

La méthode est détaillée dans [METHODOLOGIE.md](METHODOLOGIE.md).

## Utilisation

Le projet ne fournit aucun service hébergé : chacun l'utilise sur son poste, avec son propre compte Claude.

Prérequis : [Git](https://git-scm.com/), [Python 3](https://www.python.org/), [Claude Code](https://www.claude.com/product/claude-code) avec un abonnement qui y donne accès.

```
git clone https://github.com/projets-Gan/claud-ubitatif.git
cd claud-ubitatif
python -m pip install -r requirements.txt
claude
```

Puis, dans Claude Code :

- « Utilise l'agent verificateur pour vérifier : *le taux de chômage a doublé en un an* »
- « Utilise l'agent curateur pour ajouter cette source : *https://…* »

Aucune clé API n'est nécessaire. Si la variable d'environnement `ANTHROPIC_API_KEY` est définie sur votre poste, Claude Code facture l'usage à l'API au lieu de votre abonnement.

## Organisation du dépôt

| Dossier ou fichier | Contenu |
|---|---|
| `.claude/agents/` | Définition des agents Vérificateur et Curateur |
| `corpus/` | Fiches sources, fiches faits et index généré |
| `config/` | Thèmes, pays, types de sources, verdicts |
| `schemas/` | Schémas JSON des fiches |
| `modeles/` | Modèles de fiches à copier |
| `scripts/` | Validation du corpus et génération de l'index |
| `eval/` | Affirmations de test au verdict connu |

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md). Pour proposer une source sans toucher au code, ouvrez une Issue « Proposer une source ».

## Licences

- **Code** (scripts, schémas, workflows) : [Apache-2.0](LICENSE).
- **Contenu du corpus** (fiches de sources et de faits, configuration éditoriale, méthodologie) : [Licence Ouverte 2.0 (Etalab)](LICENSE-CONTENU).
- Les documents et articles cités restent la propriété de leurs auteurs ; le projet n'en conserve que des liens, des métadonnées et de courts extraits.
