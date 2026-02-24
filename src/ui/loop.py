import curses

from src.core.board import Board
from src.input.handler import handleKeyboard, handleMouse
from src.ui.colors import initColors
from src.ui.renderer import (
    drawBoard,
    drawBorder,
    drawGameOver,
    drawHUD,
    drawTitle,
    drawWin,
)
from utils.timer import getElapsed, resetTimer, startTimer


def run(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(False)
    stdscr.timeout(500)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    initColors()

    board = Board()
    startTimer()
    cursorX = 0
    cursorY = 0

    while True:
        stdscr.erase()
        drawTitle(stdscr)
        drawBorder(stdscr)
        drawBoard(stdscr, board, cursorX, cursorY)
        drawHUD(stdscr, board, getElapsed())

        if board.gameOver:
            drawGameOver(stdscr)
        if board.WIN:
            drawWin(stdscr)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_MOUSE:
            result = handleMouse(board)
            if result and result[0] == "move":
                cursorX = result[1]
                cursorY = result[2]
        else:
            cursorX, cursorY, action = handleKeyboard(key, board, cursorX, cursorY)
            if action == "quit":
                break
            if action == "restart":
                board = Board()
                resetTimer()
                startTimer()
                cursorX = 0
                cursorY = 0

        if not board.gameOver and not board.WIN:
            board.checkWin()
