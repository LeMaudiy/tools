#!/bin/bash

# Vérification des arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <fichier1> <fichier2> <fichier_sortie>"
    exit 1
fi

# Fusionner les fichiers sans doublons
sort -u "$1" "$2" > "$3"

echo "Fusion terminée. Résultat dans $3"
