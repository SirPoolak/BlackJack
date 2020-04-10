import os
import random
from Plateau import PlateauJeu

mon_plateau = PlateauJeu()

class ChoixJoueur():
    def __init__(self):
        pass

    # La fonction mise
    def mise(self, tune):
        i = 0
        while True: #la boucle pour que la mise soit un int() et inferieure a l'argent du joueur.
            try:
                while i < 1:
                    print('vous avez', tune,'€\n')
                    mise = int(input('Quel est votre mise? '))
                    if mise <= tune and mise != 0:
                        i += 1
                    elif mise == 0:
                        mon_plateau.clear_window()
                        print('Votre mise doit être superieur à 0!')
                    else:
                        mon_plateau.clear_window()
                        print('Votre mise doit être inferieur à votre argent!')
            except:
                mon_plateau.clear_window()
                print("La mise doit être écrite en chiffres et sans virgule!")
            else:
                break
        return mise

    # Les regles du jeu
    def help(self):
        i=0
        while i < 1:
            mon_plateau.clear_window()
            print("\tREGLES DU JEU\n")
            print("La partie oppose individuellement chaque joueur contre la banque.")
            print("Le but est de battre le croupier sans dépasser 21. Dès qu'un joueur fait plus que 21,")
            print("on dit qu'il « Brûle » ou qu'il « crève » et il perd sa mise initiale.")
            print("La valeur des cartes est établie comme suit :")
            print("  • de 2 à 9 → valeur nominale de la carte")
            print("  • chaque figure + le 10 surnommées « bûche » → 10 points")
            print("  • l'As → 1 ou 11 (au choix)\n")
            print("Victoire avec un BLACK JACK : Si le joueur à un As et une « bûche » dans les deux premières\ncartes il gagne directement la manche, il remporte 1,5 fois sa mise\n")
            print("Les choix du joueus:")
            print('  "Carte"    -> Tirer une nouvelle carte, si le joueur depasse le 21 il perd sa mise.')
            print(' "Doubler"   -> Après avoir reçu deux cartes, le joueur peut choisir de doubler sa mise\n                à la seule condition de ne recevoir qu'"'"'une carte après cela.')
            print('  "Reste"    -> Le joueur garde sa main et c'"'"'est au croupier de piocher les cartes.')
            print('"Abondonner" -> Le joueur abondonne cette manche et perd la moité de sa mise.\n\n')

            retour = input('"Retour" -> Pour revenir a la partie: ')
            if retour.lower() == 'retour' or retour.lower() == 'r':
                i += 1

    # Fonction jouer pour demander au joueur s'il veut continuer a jouer
    def jouer(self):
        i = 0
        while i < 1:
            print('Voulez vous continuer? (Oui/Non)')
            play = input()
            mon_plateau.clear_window()
            if play.lower() == 'oui' or play.lower() == 'o':
                i += 1
                return True
            elif play.lower() == 'non' or play.lower() == 'n':
                mon_plateau.quit()

    # Fonction qui affiche les deifferents choix du joueur en fonction du tour
    def propositions(self, nbtours, rep_joueur='0', tune='0',mise='0'):
        if nbtours < 1 and mise*2 <= (tune + mise) :
            print('"Carte"      -> Tirer une nouvelle carte')
            print('"Doubler"    -> Doubler votre mise')
            print('"Reste"      -> Garder votre main')
            print('"Abondonner" -> Vous abbondonez cette manche')
            print('"Quit"       -> Quitter le jeux')
            print('"Help"       -> Voir les regles du jeu')
        elif nbtours >= 1 and nbtours < 10 and mise*2 < (tune + mise):
            print('"Carte"      -> Tirer une nouvelle carte')
            print('"Reste"      -> Garder votre main')
            print('"Abondonner" -> Vous abondonez cette manche')
            print('"Quit"       -> Quitter le jeux')
            print('"Help"       -> Voir les regles du jeu')
        elif  nbtours < 10 and mise*2 > (tune + mise):
            print('"Carte"      -> Tirer une nouvelle carte')
            print('"Reste"      -> Garder votre main')
            print('"Abondonner" -> Vous abondonez cette manche')
            print('"Quit"       -> Quitter le jeux')
            print('"Help"       -> Voir les regles du jeu')
            if rep_joueur.lower() == 'doubler' or rep_joueur.lower() == 'd':
                print('Vous ne pouvez pas doubler!')
        elif nbtours >= 10 and nbtours < 20:
            print('Votre argent:', tune,'€')

    # Fonction Game Over, demande au joueur de recommencer une nouvelle partie après la défaite
    def game_over(self):
        print('GAME OVER!')
        i = 0
        while i < 1:
            print('Voulez vous recommencer? (Oui/Non)')
            play = input()
            mon_plateau.clear_window()
            if play.lower() == 'oui' or play.lower() == 'o':
                i += 1
                return True
            elif play.lower() == 'non' or play.lower() == 'n':
                mon_plateau.quit()
