import curses
from src.core.board import COLS, ROWS

def handleKeyboard(key, board, cursorX, cursorY):
    newX, newY = cursorX, cursorY
    action = None

    if key == curses.KEY_UP:
        newY = max(0, cursorY - 1)
    elif key == curses.KEY_DOWN:
        newY = min(ROWS - 1, cursorY + 1)
    elif key == curses.KEY_LEFT:
        newX = max(0, cursorX - 1)
    elif key == curses.KEY_RIGHT:
        newX = min(COLS - 1, cursorX + 1)
    elif key in [ord('\n'), ord(' '), curses.KEY_ENTER]:
        action = "reveal"
    elif key in [ord('f'), ord('F')]:
        action = "flag"
    elif key in [ord('r'), ord('R')]:
        action = "restart"
    elif key in [ord('q'), ord('Q')]:
        action = "quit"

    if action == "reveal" and not board.gameOver and not board.WIN:
        board.reveal(cursorX, cursorY)
    elif action == "flag" and not board.gameOver and not board.WIN:
        board.flag(cursorX, cursorY)

    return newX, newY, action

def handleMouse(board):
    from src.ui.renderer import OFFSET_X, OFFSET_Y, CELL_W
    from src.core.board import COLS, ROWS
    action = None
    try:
        _, mx, my, _, bstate = curses.getmouse()
        col = (mx - OFFSET_X) // CELL_W
        row = my - OFFSET_Y
        if 0 <= col < COLS and 0 <= row < ROWS:
            if bstate & curses.BUTTON1_CLICKED:
                if not board.gameOver and not board.WIN:
                    board.reveal(col, row)
                action = ("move", col, row)
            elif bstate & curses.BUTTON3_CLICKED:
                if not board.gameOver and not board.WIN:
                    board.flag(col, row)
                action = ("move", col, row)
    except curses.error:
        pass
    return action
