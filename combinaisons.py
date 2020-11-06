#!/usr/bin/env python3

import pandas as pd
from traitements import decompo_valeur_couleur, convert_integer



def paire(tirage_final):
    '''
    Vérifie la combinaison "Paire" :
        Récupère les valeurs des cartes uniques et compte le nombre de cartes pour chacune de ces valeurs
        S'il y a 4 valeurs uniques et que la liste du compte des cartes par leur valeur triée est [1, 1, 1, 2]
        La valeur retournée est True

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen
    '''
    valeur, couleur = decompo_valeur_couleur(tirage_final)
    valeurs_uniques = pd.Series(valeur).unique()

    compte_valeur_carte = []

    for i in valeurs_uniques:
        compte_valeur_carte.append(valeur.count(i))

    if len(valeurs_uniques) == 4 and sorted(compte_valeur_carte) == [1, 1, 1, 2]:
        return True

    else:
        return False



def double_paire(tirage_final):
    '''
    Vérifie la combinaison "Double Paire" :
        Récupère les valeurs des cartes uniques et compte le nombre de cartes pour chacune de ces valeurs
        S'il y a 3 valeurs uniques et que la liste du compte des cartes par leur valeur triée est [1, 2, 2]
        La valeur retournée est True

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen
    '''
    valeur, couleur = decompo_valeur_couleur(tirage_final)
    valeurs_uniques = pd.Series(valeur).unique()

    compte_valeur_carte = []

    for i in valeurs_uniques:
        compte_valeur_carte.append(valeur.count(i))

    if len(valeurs_uniques) == 3 and sorted(compte_valeur_carte) == [1, 2, 2]:
        return True

    else:
        return False



def brelan(tirage_final):
    '''
    Vérifie la combinaison "Brelan" :
        Récupère les valeurs des cartes uniques et compte le nombre de cartes pour chacune de ces valeurs
        S'il y a 3 valeurs uniques et que la liste du compte des cartes par leur valeur triée est [1, 1, 3]
        La valeur retournée est True

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen
    '''
    valeur, couleur = decompo_valeur_couleur(tirage_final)
    valeurs_uniques = pd.Series(valeur).unique()

    compte_valeur_carte = []

    for i in valeurs_uniques:
        compte_valeur_carte.append(valeur.count(i))

    if len(valeurs_uniques) == 3 and sorted(compte_valeur_carte) == [1, 1, 3]:
        return True

    else:
        return False



def quinte(tirage_final):
    '''
    Vérifie la combinaison "Quinte" :
        Récupère la valeur des cartes, les convertit en INTEGER, les trie et compare la valeur de chaque carte à celle de la suivante
        Si la valeur de la carte est égale à celle de la suivante, True est ajouté dans un tableau
        Retourne True si le tableau comporte 4 True ou que la liste triée des valeurs des cartes est [1, 10, 11, 12, 13]

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen    
    '''
    valeur = convert_integer(tirage_final)
    valeur.sort()

    suite = []
    for i, j in zip(valeur, range(len(valeur)-1)):
        if i == valeur[j+1]-1:
            suite.append(True)

    if suite.count(True) == 4 or valeur == [1, 10, 11, 12, 13]:
        return True

    else :
        return False



def flush(tirage_final):
    '''
    Vérifie la combinaison "Flush" :
        Récupère la couleur des cartes et compte si la couleur de la première carte est égale au nombre des cartes
        Retourne True si c'est le cas

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen   
    '''
    valeur, couleur = decompo_valeur_couleur(tirage_final)

    if couleur.count(couleur[0]) == len(couleur):
        return True

    else:
        return False



def full(tirage_final):
    '''
    Vérifie la combinaison "Full" :
        Récupère les valeurs des cartes uniques et compte le nombre de cartes pour chacune de ces valeurs
        S'il y a 2 valeurs uniques et que la liste du compte des cartes par leur valeur triée est [2, 3]
        La valeur retournée est True

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen  
    '''
    valeur, couleur = decompo_valeur_couleur(tirage_final)
    valeurs_uniques = pd.Series(valeur).unique()

    compte_valeur_carte = []

    for i in valeurs_uniques:
        compte_valeur_carte.append(valeur.count(i))

    if len(valeurs_uniques) == 2 and sorted(compte_valeur_carte) == [2, 3]:
        return True

    else:
        return False



def carre(tirage_final):
    '''
    Vérifie la combinaison "Carré" :
        Récupère la couleur des cartes et compte le nombre de cartes possédant la/les couleurs
        S'il y a 2 couleurs et que la liste du compte des cartes par leur couleur triée est [1, 4]
        La valeur retournée est True

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen  
    '''
    valeur, couleur = decompo_valeur_couleur(tirage_final)
    valeurs_uniques = pd.Series(valeur).unique()

    compte_valeur_carte = []

    for i in valeurs_uniques:
        compte_valeur_carte.append(valeur.count(i))

    if len(valeurs_uniques) == 2 and sorted(compte_valeur_carte) == [1, 4]:
        return True

    else:
        return False



def quinte_flush(tirage_final):
    '''
    Vérifie la combinaison "Quinte Flush"
        Si les combinaisons Quinte et Fush retournent True, la valeur retournée est True

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen    
    '''
    if quinte(tirage_final) == True and flush(tirage_final) == True:
        return True

    else:
        return False



def quinte_flush_royale(tirage_final):
    '''
    Vérifie la combinaison "Quinte Flush Royale" :
        Vérifie l'obtention des combinaisons Quinte et Flush
        Puis si la liste des valeurs des cartes triées est [1, 10, 11, 12, 13]
        La valeur retournée est True

    Param :
        - tirage_final: Une liste

    Sortie :
        Un booléen    
    '''
    if quinte(tirage_final) == True and flush(tirage_final) == True:
        valeur = convert_integer(tirage_final)
        if sorted(valeur) == [1, 10, 11, 12, 13]:
            return True

    else:
        return False