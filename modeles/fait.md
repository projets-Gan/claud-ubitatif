---
# Modèle de fiche FAIT. Copier ce fichier vers :
#   corpus/faits/<premier-theme>/<id>.md
# et remplacer toutes les valeurs. Les lignes commençant par # peuvent être supprimées.
id: theme-sujet-periode                      # identique au nom du fichier, ASCII, minuscules, tirets
type_fiche: fait
enonce: "Phrase factuelle et précise : chiffre, unité, période, périmètre."
valeur: null                                 # facultatif : nombre principal
unite: null                                  # facultatif : %, milliards d'euros, personnes…
definition: "Mesure ou définition utilisée (ex. chômage au sens du BIT)."
periode: "2026"                              # AAAA, AAAA-MM, AAAA-T1 à T4 ou AAAA-MM-JJ
themes: [emploi]
sous_themes: []
pays: [FR]
etat_donnee: null                            # statistique : provisoire ou definitif (obligatoire si 1 seule source N1)
statut: en-attente                           # valide (1 source N1, ou 2 sources N2+ indépendantes), en-attente, conteste
date_validite: 2026-12-31                    # date de la prochaine publication qui pourrait le modifier
sources:
  - source: id-de-la-premiere-source
    extrait: "Court extrait qui appuie le fait."
    localisation: "page, tableau ou paragraphe"   # obligatoire si 1 seule source N1
  - source: id-de-la-seconde-source-independante
    extrait: "Court extrait qui appuie le fait."
contredit_par: []                            # obligatoire si statut = conteste
notes: ""
---

## Contexte

Ce que le fait signifie, à quoi le comparer (évolution, autres pays), pièges fréquents
(confusion de définitions, de périmètres ou de périodes).

## Limites

Révisions attendues, marge d'erreur, éléments que les sources ne couvrent pas.
