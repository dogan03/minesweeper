import curses

_colors = {}

def initColors():
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_CYAN, -1)
    curses.init_pair(3, curses.COLOR_RED, -1)
    curses.init_pair(4, curses.COLOR_GREEN, -1)
    curses.init_pair(5, curses.COLOR_BLUE, -1)
    curses.init_pair(6, curses.COLOR_GREEN, -1)
    curses.init_pair(7, curses.COLOR_RED, -1)
    curses.init_pair(8, curses.COLOR_CYAN, -1)
    curses.init_pair(9, curses.COLOR_MAGENTA, -1)
    curses.init_pair(10, curses.COLOR_YELLOW, -1)
    curses.init_pair(11, curses.COLOR_WHITE, -1)
    curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(13, curses.COLOR_BLACK, curses.COLOR_WHITE)

    _colors["hidden"] = curses.color_pair(1)
    _colors["empty"] = curses.color_pair(2)
    _colors["mine"] = curses.color_pair(3) | curses.A_BOLD
    _colors["flag"] = curses.color_pair(10) | curses.A_BOLD
    _colors["n1"] = curses.color_pair(5) | curses.A_BOLD
    _colors["n2"] = curses.color_pair(4) | curses.A_BOLD
    _colors["n3"] = curses.color_pair(3) | curses.A_BOLD
    _colors["n4"] = curses.color_pair(9) | curses.A_BOLD
    _colors["n5"] = curses.color_pair(7) | curses.A_BOLD
    _colors["n6"] = curses.color_pair(8) | curses.A_BOLD
    _colors["n7"] = curses.color_pair(11) | curses.A_BOLD
    _colors["n8"] = curses.color_pair(1)
    _colors["cursor"] = curses.color_pair(12) | curses.A_BOLD
    _colors["hud"] = curses.color_pair(13)
    _colors["title"] = curses.color_pair(10) | curses.A_BOLD
    _colors["gameover"] = curses.color_pair(3) | curses.A_BOLD
    _colors["win"] = curses.color_pair(4) | curses.A_BOLD

def getColors():
    return _colors
