import domino

class player:
    score = 0

    def __init__(self, name, num_dominoes, boneyard):
        self.name = name
        self.hand = hand(num_dominoes, boneyard)

class hand:
    def __init__(self, num_dominoes, boneyard):
        pass



