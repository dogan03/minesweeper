import pygame
from src.core.board import COLS, ROWS

def drawBoard(screen, board):
    for i in range(COLS):
        for j in range(ROWS):
            board.grid[i][j].drawCell(screen, i, j)

def drawHUD(screen, board, elapsed):
    pygame.draw.rect(screen, (189,189,189), (0, 640, 640, 60))
    font = pygame.font.SysFont("Arial", 24)
    flags = sum(1 for i in range(COLS) for j in range(ROWS) if board.grid[i][j].f)
    mines_left = 40 - flags
    t1 = font.render(f"Mines: {mines_left}", True, (0,0,0))
    t2 = font.render(f"Time: {elapsed}s", True, (0,0,0))
    screen.blit(t1, (10, 655))
    screen.blit(t2, (500, 655))

def drawGameOver(screen):
    font = pygame.font.SysFont("Arial", 48)
    t = font.render("GAME OVER", True, (255,0,0))
    screen.blit(t, (640//2 - t.get_width()//2, 640//2 - t.get_height()//2))

def drawWin(screen):
    font = pygame.font.SysFont("Arial", 48)
    t = font.render("YOU WIN!", True, (0,200,0))
    screen.blit(t, (640//2 - t.get_width()//2, 640//2 - t.get_height()//2))
