---
# Modèle de fiche SOURCE. Copier ce fichier vers :
#   corpus/sources/<premier-theme>/<annee-de-publication>/<id>.md
# et remplacer toutes les valeurs. Les lignes commençant par # peuvent être supprimées.
id: aaaa-mm-jj-editeur-sujet            # identique au nom du fichier, ASCII, minuscules, tirets
type_fiche: source
titre: "Titre exact du document"
editeur: "Nom de l'organisme ou du média"   # ex. INSEE, AFP, Le Monde
auteurs: []                                  # facultatif
type: donnees-officielles                    # code de config/types-sources.yaml
url: "https://exemple.fr/document"
archive: null                                # lien Wayback Machine / archive.today, ou null
hash_sha256: null                            # empreinte du document original, facultatif
date_publication: 2026-01-01
date_consultation: 2026-01-01
themes: [emploi]                             # codes de config/taxonomie.yaml ; le premier fixe le dossier
sous_themes: []                              # facultatif, doivent relever des thèmes indiqués
pays: [FR]
langue: fr
depend_de: []                                # ids des sources reprises (ex. la dépêche AFP d'origine)
notes: ""                                    # facultatif
---

## Résumé

Deux à cinq phrases, rédigées avec vos propres mots, sur ce que contient la source
et sur son périmètre (période, champ, méthode).

## Extraits

> Court extrait littéral (une ou deux phrases au plus), avec sa localisation (page, tableau).

## Points d'attention

Définitions utilisées, révisions possibles, limites méthodologiques.
