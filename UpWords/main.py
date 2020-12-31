import pyglet
import sys
from math import degrees
from pyglet.window import key

window = pyglet.window.Window(1024, 720, "UpWords", resizable=False)


class player:
    def __init__(self, name, score, turn):
        self.playerName = name
        self.playerScore = score
        self.playerTurnNo = turn

class tile: 
    def __init__(self, tileX, tileY, letter, stackVal):
        self.tileCoordinateX = tileX
        self.tileCoordinateY = tileY
        self.tileLetter = letter
        self.tileStackValue = stackVal

class gameRules: 
    def __init__(self, maxHeight, maxLetters, timeLimit, scoreLimit):
        self.maxTileHeight = maxHeight
        self.maxLettersPerPlayer = maxLetters
        self.turnTimeLimit = timeLimit
        self.maxScore = scoreLimit

class gameBoard:
    

