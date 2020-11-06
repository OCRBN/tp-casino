#!/usr/bin/env python3

import pandas as pd
from combinaisons import *



def gains(tirage_final, mise):
    '''
    Détermine les gains :
        Multiplie la valeur du gain selon la combinaison gagnante

    Param :
        - tirage_final:     Une liste
        - mise :            Un integer
    
    Sortie :
        - gain : Le gain obtenu (integer)
        - resultat : Un string spécifiant le montant du gain
    '''
    if quinte_flush_royale(tirage_final) == True:
        gain = mise*250
        resultat = "\n\nQuinte Flush Royale : Vous gagnez " + str(gain) + " euros"
        return gain, resultat

    elif quinte_flush(tirage_final) == True:
        gain = mise*50
        resultat = "\n\nQuinte Flush ! Vous gagnez " + str(gain) + " euros"
        return gain, resultat
    
    elif carre(tirage_final) == True:
        gain = mise*25
        resultat = "\n\nCarré : Vous gagnez " + str(gain) + " euros"
        return gain, resultat
    
    elif full(tirage_final) == True:
        gain = mise*9
        resultat = "\n\nFull : Vous gagnez " + str(gain) + " euros"
        return gain, resultat
    
    elif flush(tirage_final) == True:
        gain = mise*6
        resultat = "\n\nFlush : Vous gagnez " + str(gain) + " euros"
        return gain, resultat
    
    elif quinte(tirage_final) == True:
        gain = mise*4
        resultat = "\n\nQuinte : Vous gagnez " + str(gain) + " euros"
        return gain, resultat
    
    elif brelan(tirage_final) == True:
        gain = mise*3
        resultat = "\n\nBrelan : Vous gagnez " + str(gain) + " euros"
        return gain, resultat
    
    elif double_paire(tirage_final) == True:
        gain = mise*2
        resultat = "\n\nDouble Paire : Vous gagnez " + str(gain) + " euros"
        return gain, resultat
    
    elif paire(tirage_final) == True:
        gain = mise*1
        resultat = "\n\nPaire : Vous gagnez " + str(gain) + " euros"
        return gain, resultat
    
    else:
        gain = 0
        resultat = "\n\nPerdu !"
        return gain, resultat