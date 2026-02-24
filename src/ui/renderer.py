import curses

from src.core.board import COLS, ROWS
from src.ui.colors import getColors

OFFSET_Y = 3
OFFSET_X = 2
CELL_W = 3


def drawTitle(win):
    colors = getColors()
    title = "*** MINESWEEPER ***"
    try:
        win.addstr(0, OFFSET_X, title, colors["title"])
    except curses.error:
        pass


def drawBoard(win, board, cursorX, cursorY):
    colors = getColors()
    for i in range(COLS):
        for j in range(ROWS):
            cell = board.grid[i][j]
            ch = cell.getChar()
            color = cell.getColor(colors)
            screen_x = OFFSET_X + i * CELL_W
            screen_y = OFFSET_Y + j
            if i == cursorX and j == cursorY:
                color = colors["cursor"]
            try:
                win.addstr(screen_y, screen_x, f" {ch} ", color)
            except curses.error:
                pass


def drawHUD(win, board, elapsed):
    colors = getColors()
    mines_left = board.getMinesLeft()
    hud_y = OFFSET_Y + ROWS + 1
    try:
        win.addstr(
            hud_y,
            OFFSET_X,
            f" Mines left: {mines_left:<4}  Time: {elapsed:>4}s  [Arrow keys] Move  [Enter] Reveal  [F] Flag  [R] Restart  [Q] Quit ",
            colors["hud"],
        )
    except curses.error:
        pass


def drawGameOver(win):
    colors = getColors()
    msg = "  GAME OVER! You hit a mine. Press R to restart.  "
    try:
        h, w = win.getmaxyx()
        win.addstr(
            OFFSET_Y + ROWS // 2,
            max(0, w // 2 - len(msg) // 2),
            msg,
            colors["gameover"],
        )
    except curses.error:
        pass


def drawWin(win):
    colors = getColors()
    msg = "  YOU WIN! All mines cleared! Press R to restart.  "
    try:
        h, w = win.getmaxyx()
        win.addstr(
            OFFSET_Y + ROWS // 2, max(0, w // 2 - len(msg) // 2), msg, colors["win"]
        )
    except curses.error:
        pass


def drawBorder(win):
    colors = getColors()
    top_y = OFFSET_Y - 1
    bot_y = OFFSET_Y + ROWS
    left_x = OFFSET_X - 1
    right_x = OFFSET_X + COLS * CELL_W
    try:
        for j in range(ROWS + 2):
            win.addstr(top_y + j, left_x, "|", colors["hidden"])
            win.addstr(top_y + j, right_x, "|", colors["hidden"])
        for i in range(COLS * CELL_W + 2):
            win.addstr(top_y, left_x + i, "-", colors["hidden"])
            win.addstr(bot_y, left_x + i, "-", colors["hidden"])
    except curses.error:
        pass
