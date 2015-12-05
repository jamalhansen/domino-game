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

            if check_for_domino(dominoes, new_domino):
                dominoes.append(new_domino)

    return dominoes

def check_for_domino(dominoes, new_domino):
    """
    This function will check to see if new_domino exists in dominoes and
    return False if it exists.
    """
    if dominoes:
        for domino in dominoes:
            if (new_domino.dots1, new_domino.dots2) == (domino.dots1, domino.dots2):
                return False

            elif (new_domino.dots1, new_domino.dots2) == (domino.dots2, domino.dots1):
                return False

        return True

    else:
        return True
