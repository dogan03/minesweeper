import curses
from src.ui.loop import run

if __name__ == "__main__":
    curses.wrapper(run)
