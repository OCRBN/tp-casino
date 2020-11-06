#!/usr/bin/env python3

import random
from gains import gains



def premier_tirage(deck, nombre):
    '''
    Effectue un premier tirage :
        Tire au hasard un nombre de cartes dans une liste et les enlève de la liste

    Param :
        - deck :        Une liste représentant les cartes
        - nombre :      Un integer spécifiant le nombre de cartes à tirer
    
    Sortie :
        - tirage :      Une liste représantant les cartes tirées
        - deck :        Une liste représantant les cartes sans celles du tirage
    '''
    tirage = random.sample(deck, k=nombre)

    for i in tirage:
        deck.remove(i)
        
    return tirage, deck



def choix_carte(tirage):
    '''
    Permet de choisir des cartes :
        Demande au joueur de sélectionner les cartes qu'il souhaite garder d'un premier tirage

    Param :
        - tirage :      Une liste représentant les cartes du premier tirage

    Sortie :
        - jeu :         Une liste des cartes sélectionnées par le joueur
    '''
    jeu = []
    print("Souhaitez-vous garder les cartes suivantes (Oui(o) / Non(n)) :")

    for i in tirage:
        print("\n     -", i,"?")
        
        while True:
            choix = (input("---> Choix : ")).lower()
        
            if choix == "o" or choix == "n":
                if choix == "o":
                    jeu.append(i)
                break

            else:
                print("\n\n\nErreur ! Vous devez saisir \"o\" ou \"n\" ! Recommencez...")
                print("\n     -", i,"?")
                continue

    return jeu



def deuxieme_tirage(deck, jeu):
    '''
    Effectue un deuxième tirage :
        Détermine le nombre de cartes restantes à tirer en fonction du premier tirage (jeu)
        Tire au hasard le nombre de cartes restantes dans une liste (deck)

    Param :
        - deck :        Une liste représentant les cartes après le premier tirage
        - jeu :         Une liste représentant les cartes sélectionnées par le joueur au premier tirage

    Sortie :
        - tirage_final: Une liste représentant le tirage final (main) du joueur
    '''
    cartes_a_tirer = 5 - len(jeu)
    tirage_2, deck_2 = premier_tirage(deck,cartes_a_tirer)
    tirage_final = jeu + tirage_2

    return tirage_final



def machine():
    '''
    Permet d'obtenir le tirage final (main) du joueur :
        Fait appel aux fonctions :
            - premier_tirage(deck, nombre):
            - choix_carte(tirage):
            - deuxieme_tirage(deck, jeu):

    Sortie :
        - tirage_final: Une liste représentant le tirage final (main) du joueur
    '''
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

    tirage, deck_2 = premier_tirage(deck, 5)
    print("\n\n______________________________________________________________\n\n")
    print("\nVoici le premier tirage :", tirage, "\n\n")

    jeu = choix_carte(tirage)
    print("\n\nVoici votre jeu suite au premier tirage :", jeu, "\n")

    tirage_final = deuxieme_tirage(deck_2,jeu)
    print("Voici votre tirage final :", tirage_final)
    return tirage_final



def partie(bankroll, mise):
    '''
    Lance une partie :
        Effectue un tirage final et calcule le montant du gain en fonction d'une bankroll de départ et d'une mise

    Param :
        - bankroll :    Un integer
        - mise :        Un integer

    Sortie :
        - resultat :    Un string spécifiant le montant du gain
        - bankroll :    Un integer spécifiant le montant de la bankroll
    '''
    tirage_final = machine()
    gain, resultat = gains(tirage_final, mise)

    bankroll = bankroll - mise
    bankroll += gain

    return resultat, bankroll



def saisie_integer_banrkoll(demande):
    '''
    Vérifie la saisie de la Bankroll :
        Teste si la saisie est un integer et redemande la saisie si ce n'est pas le cas
    
    Param :
        - demande :     Un string spécifiant la nature de la saisie

    Sortie :
        - saisie :      Un integer représentant la Bankroll du joueur
    '''
    while True:
        try:
            saisie = int(input(demande))
            break
        except ValueError:
            print("\nErreur ! Vous devez saisir un nombre entier ! Recommencez...")
    
    return saisie



def saisie_integer_mise(demande,bankroll):
    '''
    Vérifie la saisie de la mise :
        Teste si la saisie est un integer et redemande la saisie si ce n'est pas le cas
    
    Param :
        - demande :     Un string spécifiant la nature de la saisie
        - bankroll :    Un integer représentant le montant de la Bankroll du joueur

    Sortie :
        - saisie :      Un integer représentant la mise du joueur
    '''
    while True:
        try:
            saisie = int(input(demande))
            break
        except ValueError:
            print("\nErreur ! Vous devez saisir un nombre entier ! Recommencez...")
            print("\nMontant de votre Bankroll :", bankroll)
    
    return saisie



def video_poker():
    '''
    Lance le jeu du Video Poker :
        Demande au joueur d'entrer le montant d'une bankroll et d'une mise
        Puis lui permet de jouer jusqu'à avoir tout perdu
    '''
    bankroll = saisie_integer_banrkoll("\n\n\nMontant initial de votre Bankroll : ")
    mise = saisie_integer_mise("Votre mise : ", bankroll)

    while bankroll - mise < 0:
        print("\nVous ne pouvez pas miser un montant supérieur à votre Bankroll !")
        mise = saisie_integer_mise("Votre mise : ", bankroll)


    resultat, bankroll = partie(bankroll, mise)
    print(str(resultat))
    print("\n\nMontant de votre Bankroll :", bankroll)

    if bankroll == 0:
        print("\nGame Over !\n")


    while bankroll - mise >= 0:
        print("\n\nVoulez-vous rejouer ? (Oui(o) / Non(n)")

        while True:
            rejouer = (input("---> Choix : ")).lower()
            if rejouer == "o" or rejouer == "n":
                print("\nMontant de votre Bankroll :", bankroll)
                break
            else:
                print("\n\nErreur ! Vous devez saisir \"o\" ou \"n\" ! Recommencez...\n")
                print("Montant de votre Bankroll :", bankroll)
                print("\nVoulez-vous rejouer ? (Oui(o) / Non(n)")
                continue
        
        if rejouer == "n":
            print("\nFin du jeu ! Vous repartez avec " + str(bankroll) + " euros\n\n")
            break
        
        else:
            mise = saisie_integer_mise("Votre mise : ", bankroll)
            if bankroll - mise < 0:
                print("\nVous ne pouvez pas miser un montant supérieur à votre Bankroll !")
                print("\nMontant de votre Bankroll :", bankroll)
                mise = saisie_integer_mise("Votre mise : ", bankroll)

            resultat, bankroll = partie(bankroll, mise)
            print(str(resultat))
            print("\n\nMontant de votre Bankroll :", bankroll)
         
            if bankroll == 0:
                print("\nGame Over !\n")
                break