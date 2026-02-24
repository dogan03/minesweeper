import pygame
from src.core.board import COLS, ROWS

def handleInput(event, board):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if y > 640:
            return
        i = x // 40
        j = y // 40
        if 0 <= i < COLS and 0 <= j < ROWS:
            if event.button == 1:
                if not board.grid[i][j].f:
                    board.reveal(i, j)
            elif event.button == 3:
                board.flag(i, j)
