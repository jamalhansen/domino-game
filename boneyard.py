"""
This module represents the boneyard, which is the pile of unused dominoes
"""

from domino import domino
from random import shuffle

def add_dominoes(dots):
    """
    This function will create a list containing dominoes that have up to
    a specified number of dots.

    Example:
    add_dominoes(3)

    Will return a list containing domino objects with the following dots:
    (0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2)
    (2, 3), (3, 3)
    """
    dominoes = []
    for dots1 in range(dots + 1 ):

        for dots2 in range(dots + 1):
            new_domino = domino(dots1, dots2)

            if new_domino not in dominoes:
                dominoes.append(new_domino)

    return dominoes

