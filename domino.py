class domino():
    def __init__(self, dots1, dots2):
        self.dots1 = dots1
        self.dots2 = dots2
        self.dots = (dots1, dots2)
        self.value = dots1 + dots2

    def __eq__(self, other):
        return sorted(list(self.dots)) == sorted(list(other.dots))

