from domino import domino
from random import shuffle

def add_dominoes(dots):
    dominoes = []
    for dots1 in range(dots + 1 ):

        for dots2 in range(dots + 1):
            new_domino = domino(dots1, dots2)

            if new_domino not in dominoes:
                dominoes.append(new_domino)

    return dominoes

