class boneyard():
    def __init__(self):
        self.dominoes = set(self.shuffle(6))

    def shuffle(self, dots):
        dominoes = []
        for dot1 in range(dots + 1 ):
            for dot2 in range(dots + 1):
                new_domino = domino(dot1, dot2)
                if self.check_for_domino(dominoes, new_domino):
                    dominoes.append(new_domino)
        return dominoes

    def check_for_domino(self, dominoes, new_domino):
        if dominoes:
            for domino in dominoes:
                if (new_domino.dots1, new_domino.dots2) == (domino.dots1, domino.dots2):
                    return False

                elif (new_domino.dots1, new_domino.dots2) == (domino.dots2, domino.dots1):
                    return False
                
        return True

class domino():
    def __init__(self, dots1, dots2):
        self.dots1 = dots1
        self.dots2 = dots2
        self.dots = (dots1, dots2) 
        self.value = dots1 + dots2
