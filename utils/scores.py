import json
import os
import time

SCORES_FILE = os.path.join(os.path.dirname(__file__), "../data/scores.json")

def loadScores():
    if not os.path.exists(SCORES_FILE):
        return []
    try:
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def saveScore(elapsed, difficulty="medium"):
    scores = loadScores()
    entry = {
        "time": elapsed,
        "difficulty": difficulty,
        "date": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    scores.append(entry)
    scores.sort(key=lambda x: x["time"])
    try:
        with open(SCORES_FILE, "w") as f:
            json.dump(scores, f, indent=2)
    except:
        pass

def getBestScore(difficulty="medium"):
    scores = loadScores()
    filtered = [s for s in scores if s.get("difficulty") == difficulty]
    if not filtered:
        return None
    return min(filtered, key=lambda x: x["time"])

def getTopScores(n=10, difficulty="medium"):
    scores = loadScores()
    filtered = [s for s in scores if s.get("difficulty") == difficulty]
    filtered.sort(key=lambda x: x["time"])
    return filtered[:n]

def clearScores():
    try:
        with open(SCORES_FILE, "w") as f:
            json.dump([], f)
    except:
        pass
