import random
from src.core.cell import c

COLS = 16
ROWS = 16
MINES = 40

class Board:
    def __init__(self):
        self.COLS = COLS
        self.ROWS = ROWS
        self.MINES = MINES
        self.gameOver = False
        self.WIN = False
        self.firstClick = True
        self.flagCount = 0

        self.grid = [[c(i, j) for j in range(self.ROWS)] for i in range(self.COLS)]

        positions = random.sample(range(self.COLS * self.ROWS), self.MINES)
        for pos in positions:
            col = pos % self.COLS
            row = pos // self.COLS
            self.grid[col][row].m = True

        for i in range(self.COLS):
            for j in range(self.ROWS):
                if not self.grid[i][j].m:
                    count = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < self.COLS and 0 <= nj < self.ROWS:
                                if self.grid[ni][nj].m:
                                    count += 1
                    self.grid[i][j].n = count

    def reveal(self, i, j):
        if i < 0 or i >= self.COLS or j < 0 or j >= self.ROWS:
            return
        cell = self.grid[i][j]
        if cell.r or cell.f:
            return
        cell.r = True
        if cell.m:
            self.gameOver = True
            for x in range(self.COLS):
                for y in range(self.ROWS):
                    if self.grid[x][y].m:
                        self.grid[x][y].r = True
            return
        if cell.n == 0:
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    self.reveal(i + di, j + dj)

    def flag(self, i, j):
        cell = self.grid[i][j]
        if not cell.r:
            was_flagged = cell.f
            cell.f = not cell.f
            if was_flagged:
                self.flagCount -= 1
            else:
                self.flagCount += 1

    def checkWin(self):
        for i in range(self.COLS):
            for j in range(self.ROWS):
                cell = self.grid[i][j]
                if not cell.m and not cell.r:
                    return False
        self.WIN = True
        return True

    def getMinesLeft(self):
        return self.MINES - self.flagCount

    def revealAll(self):
        for i in range(self.COLS):
            for j in range(self.ROWS):
                if self.grid[i][j].m:
                    self.grid[i][j].r = True
