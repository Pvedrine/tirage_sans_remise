#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def shuffle(liste):
    tmp = list()
    # Shuffle change de place les données dans la liste aléatoirement
    random.shuffle(liste)
    for i in range(0, len(liste)):
        rand_elt = random.sample(liste, 1)  # On prend un nom aléatoire parmi les entrées
        tmp.append(rand_elt[0])  # Ajout à un deuxieme index
        liste.remove(rand_elt[0])  # Suppression de la premiere liste (sans remise)
    return tmp


if __name__ == '__main__':
    # Liste des couleurs des ordis a rajouter pour compléter (toujours 8 joueurs)
    tbl = ["Bleu", "Rouge", "Vert", "Jaune", "Cyan", "Rose", "Gris ", "Orange"]

    # On prend les noms en entrée, séparés par des espaces
    chaps = [x for x in input("Donne les noms:\n").split()]
    taille_chaps = len(chaps)

    #  Maximum 8 joueurs
    if len(chaps) > 8:
        raise ValueError('Maximum 8 joueurs')

    lst = shuffle(chaps)
    for i in range(taille_chaps, len(tbl)):
        lst.append("Ordi")  # On remplit avec des ordis

    # On double l'aléatoire
    lst_coul = shuffle(tbl)

    # Affichage
    for i in range(len(lst_coul)):
        print(str(lst_coul[i]) + " -> " + str(lst[i]))
    input()
