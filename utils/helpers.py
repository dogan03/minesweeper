import time

_start = None

def startTimer():
    global _start
    _start = time.time()

def getElapsed():
    global _start
    if _start is None:
        return 0
    return int(time.time() - _start)

def resetTimer():
    global _start
    _start = None

def getCellSize():
    return 40

def getGridDims():
    return 16, 16
