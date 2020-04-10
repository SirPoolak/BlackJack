import os
import random
import sys


class PlateauJeu():

    def __init__(self):
        pass

    # Affiche le plateau de jeux
    def plateau_jeux(self, pointsC='0', pointsJ='0', ListCartesCroupier='', ListCartesJoueur='', annonce='',mise=''):
        liste_plateau = [
        '\t      │ CROUPIER │ points:', pointsC,'\n',
        '\t      └──────────┘\n',
        'Cartes:       ', ListCartesCroupier, '\n\n',
        '\t     ', annonce, '\n',
        'Mise:', mise,'€\n',
        'Cartes:       ', ListCartesJoueur, '\n',
        '\t       ┌────────┐\n',
        '\t       │ JOUEUR │ points:', pointsJ, '\n']

        x = ''.join(liste_plateau)
        print(x)


    # efface la fenetre et affiche le nom de jeu
    def clear_window(self):
        os.system('cls')
        print('\t▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
        print('\t▀╔════════════════════╗▀')
        print('\t█║ ♦ ♥ BLACK JACK ♣ ♠ ║█')
        print('\t▄╚════════════════════╝▄')
        print('\t▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n')


    # affiche correctement une liste avec un separateur (pour afficher les cartes en main sur le plateau)
    def affiche_liste(self, list):
        x = '|'.join(list)
        return x


    # Calcul les points des cartes
    def addition_points(self, listePoints):
        points = 0
        As = 0

        for i in listePoints: # separrer les As des autres cartes
            if i == 'As':
                As +=1
            else: #On additione tout les points sans les As
                points = points + i

        if As == 1: # S'il y a 1 as dans ma liste
            points1 = points + 1
            points2 = points + 10
            if points2 > 21 : # Si As vaut 10 points et on depasse la somme de 21 points
                return points1 # As vaut 1 points
            else :
                return points2 # Sinon As vout 10 points

        elif As == 2: # S'il y a 2 as dans ma liste
            points1 = points + 1 + 1
            points2 = points + 1 + 10
            if points2 > 21 : # Si 1 As vaut 10 et un autre vaut 1 point et si on depasse la somme de 21 points
                return points1 # les deux As valent 1 point chacun
            else :
                return points2 # Sinon un as vaut 10 et l'autre 1 point

        else: # Si pas d'As dans la liste de cartes, renvoyer les points.
            return points

    # quiter le jeux
    def quit(self):
        os.system('cls')
        sys.exit()

    # En fonction des points renvoyer l'annonce a afficher sur le plateau jeux
    def affichage_victoire(self, pointsJoueur, pointsCroupier, tours):
        if (pointsJoueur > pointsCroupier and pointsJoueur < 21) or pointsCroupier > 21:
            return 'MAIN GAGNANTE'
        elif pointsJoueur < pointsCroupier or pointsJoueur > 21:
            return 'MAIN PERDANTE'
        else:
            return 'EGALITE'

    # En fonction des points renvoyer rune_joueur restante
    def calcule_victoire(self, pointsJoueur, pointsCroupier, tours, tune_joueur, mise):
        if (pointsJoueur > pointsCroupier and pointsJoueur < 21) or pointsCroupier > 21:
            tune_joueur = tune_joueur + mise + mise
            return tune_joueur
        elif pointsJoueur < pointsCroupier or pointsJoueur > 21:
            return tune_joueur
        else:
            tune_joueur = tune_joueur + mise
            return tune_joueur
