import pygame
import sys
from src.core.board import Board
from src.ui.renderer import drawBoard, drawHUD, drawGameOver, drawWin
from src.ui.input_handler import handleInput
from utils.helpers import startTimer, getElapsed, resetTimer
from config.settings import WINDOW_W, WINDOW_H, TITLE, FPS

pygame.init()
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

board = Board()
startTimer()
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if not board.gameOver and not board.WIN:
            handleInput(event, board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = Board()
                resetTimer()
                startTimer()

    if not board.gameOver and not board.WIN:
        board.checkWin()

    screen.fill((189,189,189))
    drawBoard(screen, board)
    drawHUD(screen, board, getElapsed())

    if board.gameOver:
        drawGameOver(screen)
    if board.WIN:
        drawWin(screen)

    pygame.display.flip()
