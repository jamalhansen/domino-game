import domino
import boneyard

class game:
    def __init__(self, players, boneyard):
        self.boneyard = boneyard
        self.players = players
        self.board = []

    def pickup_dominoes(self, num_dominoes, player):
        for domino in range(num_dominoes):
            self.boneyard.shuffle()
            player.hand.append(self.boneyard.dominoes.pop(0))
    

class player:
    score = 0

    def __init__(self, name):
        self.name = name
        self.hand = []
