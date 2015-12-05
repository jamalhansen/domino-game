from domino import domino
from random import shuffle

def add_dominoes(dots):
    dominoes = []
    for dots1 in range(dots + 1 ):
        
        for dots2 in range(dots + 1):
            new_domino = domino(dots1, dots2)

            if check_for_domino(dominoes, new_domino):
                dominoes.append(new_domino)

    return dominoes

def check_for_domino(dominoes, new_domino):
    if dominoes:
        for domino in dominoes:
            if (new_domino.dots1, new_domino.dots2) == (domino.dots1, domino.dots2):
                return False

            elif (new_domino.dots1, new_domino.dots2) == (domino.dots2, domino.dots1):
                return False
            
        return True
    
    else:
        return True
