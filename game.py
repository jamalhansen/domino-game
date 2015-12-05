import domino
import boneyard
from random import shuffle

class game:
    def __init__(self, players, domino_set):
        self.boneyard = boneyard.add_dominoes(domino_set) 
        self.players = players
        self.board = []

    def pickup_dominoes(self, num_dominoes, player):
        for domino in range(num_dominoes):
            shuffle(self.boneyard)
            player.hand.append(self.boneyard.pop(0))
    

class player:
    score = 0

    def __init__(self, name):
        self.name = name
        self.hand = []
