from domino import domino

class boneyard():
    def __init__(self):
        self.dominoes = set()
        self.shuffle(6)

    def shuffle(self, dots):
        for dots1 in range(dots + 1 ):
            
            for dots2 in range(dots + 1):
                new_domino = domino(dots1, dots2)

                if self.check_for_domino(self.dominoes, new_domino):
                    self.dominoes.add(new_domino)

    def check_for_domino(self, dominoes, new_domino):
        if self.dominoes:

            for domino in self.dominoes:
            
                if (new_domino.dots1, new_domino.dots2) == (domino.dots1, domino.dots2):
                    return False

                elif (new_domino.dots1, new_domino.dots2) == (domino.dots2, domino.dots1):
                    return False
                
        return True
