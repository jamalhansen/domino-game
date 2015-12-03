class player:
    score = 0

    def __init__(self, name, num_dominoes):
        self.name = name
        self.hand = hand(num_dominoes)

class hand:
    def __init__(self, num_dominoes):
        self.dominoes = set()


