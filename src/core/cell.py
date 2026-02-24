class c:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.m = False
        self.r = False
        self.f = False
        self.n = 0

    def getChar(self):
        if self.f:
            return "F"
        if not self.r:
            return "#"
        if self.m:
            return "*"
        if self.n == 0:
            return "."
        return str(self.n)

    def getColor(self, colors):
        if self.f:
            return colors["flag"]
        if not self.r:
            return colors["hidden"]
        if self.m:
            return colors["mine"]
        if self.n == 0:
            return colors["empty"]
        num_colors = [
            colors["n1"], colors["n2"], colors["n3"], colors["n4"],
            colors["n5"], colors["n6"], colors["n7"], colors["n8"]
        ]
        return num_colors[self.n - 1]

    def toggle_flag(self):
        if not self.r:
            self.f = not self.f

    def isRevealed(self):
        return self.r

    def isMine(self):
        return self.m

    def isFlagged(self):
        return self.f

    def adjacentCount(self):
        return self.n
