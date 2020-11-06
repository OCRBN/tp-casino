#!/usr/bin/env python3



def decompo_valeur_couleur(tirage_final):
    '''
    Décompose les cartes en fonction de leur valeur et de leur couleur :
        Récupère la valeur et la couleur de chaque carte grâce à l'index splité par "-" et les rajoute à la liste correspondante

    Param :
        - tirage_final: Une liste

    Sortie :
        2 listes 
    '''
    valeur = []
    couleur = []

    for i in tirage_final:
        valeur.append(i.split('-')[0])
        couleur.append(i.split('-')[1])
    
    return valeur, couleur



def convert_integer(tirage_final):
    '''
    Convertit la valeur des cartes en INTEGER :
        Récupère la valeur des cartes et les convertit en INTEGER en gérant les J, Q, K et A

    Param :
        - tirage_final: Une liste

    Sortie :
        - valeur :      Une liste
    '''
    valeur, couleur = decompo_valeur_couleur(tirage_final)

    for k,i in zip(valeur, range(5)):
        try:
            valeur[i] = int(k)
        except:
            if k == "J":
                valeur[i] = 11

            if k == "Q":
                valeur[i] = 12

            if k == "K":
                valeur[i] = 13

            if k == "A":
                valeur[i] = 1

            else:
                continue

    return valeur