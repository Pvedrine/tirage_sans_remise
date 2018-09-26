#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

lst = []
# On prend les noms en entrée, séparés par des espaces
chaps = [x for x in input("Donne les noms:\n").split()]

# Shuffle change de place les données dans la liste aléatoirement
random.shuffle(chaps)
taille_chaps = len(chaps)
# Liste des couleurs des ordis a rajouter pour compléter (toujours 8 joueurs)
tbl = ["Bleu", "Rouge", "Vert", "Jaune", "Cyan", "Rose", "Gris ", "Orange"]
taille = (len(tbl))

for i in range(0, len(chaps)):  # Minimum 2 joueurs
    rand0 = random.sample(chaps, 1)  # On prend un nom aléatoire parmi les entrées
    lst.append(rand0[0])  # Ajout à un deuxieme index
    chaps.remove(rand0[0])  # Suppression de la premiere liste (sans remise)

for i in range(taille_chaps, taille):
    lst.append("Ordi")  # On remplit avec des ordis

# On double l'aléatoire
lst_coul = list()
for m in range(0, taille):
    rand = random.sample(tbl, 1)  # prends une couleur aléatoire dans la liste
    lst_coul.append(rand[0])

final = ""
for i in range(len(tbl)):
    print(str(lst_coul[i]) + " -> " + str(lst[i]))

input()
