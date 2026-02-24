import time

_start_time = None
_paused = False
_pause_offset = 0

def startTimer():
    global _start_time, _paused, _pause_offset
    _start_time = time.time()
    _paused = False
    _pause_offset = 0

def resetTimer():
    global _start_time, _paused, _pause_offset
    _start_time = None
    _paused = False
    _pause_offset = 0

def getElapsed():
    global _start_time, _pause_offset
    if _start_time is None:
        return 0
    return int(time.time() - _start_time) + _pause_offset

def formatTime(seconds):
    mins = seconds // 60
    secs = seconds % 60
    if mins > 0:
        return f"{mins}m{secs:02d}s"
    return f"{seconds}s"

def isRunning():
    return _start_time is not None
