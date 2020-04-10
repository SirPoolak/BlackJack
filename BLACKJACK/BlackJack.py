import os
import random
import sys
from Jeu_De_Cartes import JeuDeCartes
from Choix import ChoixJoueur
from Plateau import PlateauJeu

mon_plateau = PlateauJeu()
mon_paquet = JeuDeCartes()
joueur = ChoixJoueur()

def game():

    tune_joueur = 1000

    # Boucle pour continuer a jouer jusqu'à que le joueur perde la partie (tune_joueur arrive à 0)
    while tune_joueur >= 1:

        cartesJoueurPoints = []
        cartesJoueurAffiche = []
        cartesCroupierPoints = []
        cartesCroupierAffiche = []
        TourJoueur = 0
        Victoire_BlackJack = ''
        paquet = mon_paquet.jeu_de_carte()

        mon_plateau.clear_window()

        # Joueur indique combien il veux miser
        mise_joueur = joueur.mise(tune_joueur)
        # On soustrait la mise de la tune_joueur
        tune_joueur = tune_joueur - mise_joueur

        # On donne deux cartes au joueur et une au croupier
        mon_paquet.prendre_une_carte(paquet, cartesJoueurPoints, cartesJoueurAffiche)
        mon_paquet.prendre_une_carte(paquet, cartesCroupierPoints, cartesCroupierAffiche)
        mon_paquet.prendre_une_carte(paquet, cartesJoueurPoints, cartesJoueurAffiche)

        #On affiche tout le plateau de jeu
        mon_plateau.clear_window()
        mon_plateau.plateau_jeux(str(mon_plateau.addition_points(cartesCroupierPoints)), str(mon_plateau.addition_points(cartesJoueurPoints)), mon_plateau.affiche_liste(cartesCroupierAffiche), mon_plateau.affiche_liste(cartesJoueurAffiche),str(''),str(mise_joueur))

        # On affiche les les choix possibles du joueur pendant son 1er tour
        joueur.propositions(TourJoueur, '', tune_joueur, mise_joueur)

        # Victoire BLACK JACK (Si dans la main de départ on à un As et une buche on gagne la partie)
        if (cartesJoueurPoints[0] == 'As' or cartesJoueurPoints[1] == 'As') and (mon_plateau.addition_points(cartesJoueurPoints) - 10) == 10 and cartesCroupierPoints[0] != 'As':
            Victoire_BlackJack = 'BLACK JACK'
            TourJoueur += 30 #Permet de passer a la partie -> continuer le jeux?

            # On affiche le plateau avec la victoire
            mon_plateau.clear_window()
            mon_plateau.plateau_jeux(str(mon_plateau.addition_points(cartesCroupierPoints)), str(mon_plateau.addition_points(cartesJoueurPoints)), mon_plateau.affiche_liste(cartesCroupierAffiche), mon_plateau.affiche_liste(cartesJoueurAffiche),str(Victoire_BlackJack),str(mise_joueur))

            tune_joueur = tune_joueur + mise_joueur + mise_joueur + mise_joueur/2 #Calcul de la tune restante au joueur

        # Boucle des differents choix du joueur
        while TourJoueur <= 9:

            # Joueur fait un choix de reponse
            reponse_joueur = input('\nEcrivez votre choix : ')

            # Quiter le jeux
            if reponse_joueur.lower() == 'quit' or reponse_joueur.lower() == 'q':
                mon_plateau.quit()

            # Voir les regles du jeu
            elif reponse_joueur.lower() == 'help' or reponse_joueur.lower() == 'h':
                mon_plateau.clear_window()
                joueur.help()

            # Abbandoner la manche avec l'option de quiter la partie
            elif reponse_joueur.lower() == 'abondonner' or reponse_joueur.lower() == 'a':
                TourJoueur += 20 #passer a la parte -> continuer le jeux?
                tune_joueur = tune_joueur + mise_joueur/2 #Calcul de la tune restante au joueur

            # Piocher une carte
            elif reponse_joueur.lower() == 'carte' or reponse_joueur.lower() == 'c':
                mon_paquet.prendre_une_carte(paquet, cartesJoueurPoints, cartesJoueurAffiche) #Piochier une carte
                if mon_plateau.addition_points(cartesJoueurPoints) > 21 : # Si le total des points des cartes depasse le 21 :
                    TourJoueur += 10 #passer à l'étape de Victoire/Défaite
                else:
                    TourJoueur += 1 #On rajoute un tour pour que le joueur ne puisse pas doubler aux tours suivants

            # Doubler la mise seulement au 1er tour ou seulement si la mise < tune_joueur restante
            elif reponse_joueur.lower() == 'doubler' or reponse_joueur.lower() == 'd' and TourJoueur < 1 and mise_joueur*2 <= (tune_joueur + mise_joueur) :
                mon_paquet.prendre_une_carte(paquet, cartesJoueurPoints, cartesJoueurAffiche) #Piochier une carte
                if mon_plateau.addition_points(cartesJoueurPoints) > 21 : # Si le total des points des cartes depasse le 21 :
                    TourJoueur += 10 #passer à l'étape de Victoire/Défaite
                else:
                    while mon_plateau.addition_points(cartesCroupierPoints) < 16 : #Boucle pour faire piocher le croupier jusqu'à un minimum de 17 points
                        mon_paquet.prendre_une_carte(paquet, cartesCroupierPoints, cartesCroupierAffiche) #Piochier une carte
                    TourJoueur += 10 #passer à l'étape de Victoire/Défaite
                mise_joueur = mise_joueur*2 #Doubler la mise
                tune_joueur = tune_joueur - mise_joueur/2 #Calcul de la tune restante au joueur

            # Le joueur garde la main
            elif reponse_joueur.lower() == 'reste' or reponse_joueur.lower() == 'r':
                while mon_plateau.addition_points(cartesCroupierPoints) < 16 : #Boucle pour faire piocher le croupier jusqu'à un minimum de 17 points
                    mon_paquet.prendre_une_carte(paquet, cartesCroupierPoints, cartesCroupierAffiche) #Piochier une carte
                TourJoueur += 10 #passer à l'étape de Victoire/Défaite

            # Affichage ecran
            mon_plateau.clear_window()
            mon_plateau.plateau_jeux(str(mon_plateau.addition_points(cartesCroupierPoints)), str(mon_plateau.addition_points(cartesJoueurPoints)), mon_plateau.affiche_liste(cartesCroupierAffiche), mon_plateau.affiche_liste(cartesJoueurAffiche),str(''),str(mise_joueur))
            joueur.propositions(TourJoueur, reponse_joueur, tune_joueur, mise_joueur) # Affiche les propositions en fonction des tours


            # étape de Victoire/Défaite:
        if TourJoueur < 20:
            # Veirfication d'affichage sur Plateau
            resultat_victoire = mon_plateau.affichage_victoire(mon_plateau.addition_points(cartesJoueurPoints), mon_plateau.addition_points(cartesCroupierPoints), TourJoueur)
            # On calcule la tune_joueur restante en fonction de Victoire ou defaite
            tune_joueur = mon_plateau.calcule_victoire(mon_plateau.addition_points(cartesJoueurPoints), mon_plateau.addition_points(cartesCroupierPoints), TourJoueur, tune_joueur, mise_joueur)

            # Afficher le plateau
            mon_plateau.clear_window()
            mon_plateau.plateau_jeux(str(mon_plateau.addition_points(cartesCroupierPoints)), str(mon_plateau.addition_points(cartesJoueurPoints)), mon_plateau.affiche_liste(cartesCroupierAffiche), mon_plateau.affiche_liste(cartesJoueurAffiche),str(resultat_victoire),str(mise_joueur))

            # une phrase pour confirmer au joueur qu'il a bien doublé sa mise
            if reponse_joueur.lower() == 'doubler' or reponse_joueur.lower() == 'd':
                print('\nVous avez douber votre mise')

            # étape de Défaite abondon:
        elif TourJoueur >= 20 and TourJoueur <= 29:
            # une phrase pour confirmer au joueur qu'il a bien abondonné
            if reponse_joueur.lower() == 'abondonner' or reponse_joueur.lower() == 'a':
                print('\nVous avez abondonné vous gardez la moité de votre mise')

        print('Votre argent:', tune_joueur,'€\n')# Afficher la tone_joueur restante
        joueur.jouer()#proposition de continuer ou pas ?

    # GAME_OVER demande de recommencer une nouvelle partie dès le début
    if joueur.game_over() == True:
        return game()



game()
