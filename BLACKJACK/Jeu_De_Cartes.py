import os
import random

class JeuDeCartes():

    def __init__(self):
        pass


    # Liste de toutes les 52 cartes d'un pacquet de jeu de cartes
    def jeu_de_carte(self):
        paquet = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4 #11=Valet, 12=Dame, 13=Roi, 14=As
        random.shuffle(paquet) #On melande aleatoirement le paquet
        return paquet


    # Prendre une carte du paquet ae l'ajouter a la liste des points et a la liste d'affichage sur le plateau
    def prendre_une_carte(self, monpaquet, listePoints, listeAffiche):
        #retirer la derniere carte du paquet:
        carte = monpaquet.pop()
        #On choisit un symbole aleatoirement parmi la liste
        symboles = ['♦','♥','♣','♠']
        random.shuffle(symboles)
        mon_symbol = symboles[0]

        #donner a la carte un visuel et une valeur:
        if carte < 11 : # pour toutes les cartes de 2 à 10 leurs valeurs est le numéro de la carte
            points = carte
            visu_carte = str(carte) + mon_symbol
            listePoints.append(points)
            listeAffiche.append(visu_carte)
        elif carte == 11: # pour le valet
            points = 10
            visu_carte = 'V' + mon_symbol
            listePoints.append(points)
            listeAffiche.append(visu_carte)
        elif carte == 12: # pour la damme
            points = 10
            visu_carte = 'D' + mon_symbol
            listePoints.append(points)
            listeAffiche.append(visu_carte)
        elif carte == 13: # pour le roi
            points = 10
            visu_carte = 'R' + mon_symbol
            listePoints.append(points)
            listeAffiche.append(visu_carte)
        else: # pour l'as pas de precision de points puisqu'il vaut 10 ou 1 en fonction du jeu
            visu_carte = 'A' + mon_symbol
            listePoints.append('As')
            listeAffiche.append(visu_carte)
