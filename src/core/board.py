import random
from src.core.cell import c

COLS = 16
ROWS = 16
MINES = 40

class Board:
    def __init__(self):
        self.grid = [[c(i,j) for j in range(ROWS)] for i in range(COLS)]
        self.gameOver = False
        self.WIN = False
        self.firstClick = True
        mine_positions = random.sample(range(COLS*ROWS), MINES)
        for pos in mine_positions:
            self.grid[pos % COLS][pos // COLS].m = True
        for i in range(COLS):
            for j in range(ROWS):
                if not self.grid[i][j].m:
                    cnt = 0
                    for di in [-1,0,1]:
                        for dj in [-1,0,1]:
                            if di==0 and dj==0:
                                continue
                            ni,nj = i+di, j+dj
                            if 0<=ni<COLS and 0<=nj<ROWS:
                                if self.grid[ni][nj].m:
                                    cnt+=1
                    self.grid[i][j].n = cnt

    def reveal(self, i, j):
        if i<0 or i>=COLS or j<0 or j>=ROWS:
            return
        cell = self.grid[i][j]
        if cell.r or cell.f:
            return
        cell.r = True
        if cell.m:
            self.gameOver = True
            for x in range(COLS):
                for y in range(ROWS):
                    if self.grid[x][y].m:
                        self.grid[x][y].r = True
            return
        if cell.n == 0:
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if di==0 and dj==0:
                        continue
                    self.reveal(i+di, j+dj)

    def checkWin(self):
        for i in range(COLS):
            for j in range(ROWS):
                cell = self.grid[i][j]
                if not cell.m and not cell.r:
                    return False
        self.WIN = True
        return True

    def flag(self, i, j):
        cell = self.grid[i][j]
        if not cell.r:
            cell.f = not cell.f
