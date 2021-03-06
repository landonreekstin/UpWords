import pyglet
import sys
from math import degrees
from pyglet.window import key

class player:
    def __init__(self, name, score, turn):
        self.playerName = name
        self.playerScore = score
        self.playerTurnNo = turn
        self.playerLetterInventory = []


class tile: 
    def __init__(self, tileX, tileY, height, width, color, batch, letter, stackVal):
        self.tileCoordinateX = tileX
        self.tileCoordinateY = tileY
        self.tileHeight = height
        self.tileWidth = width
        self.tileColor = color
        self.tileBatch = batch
        self.tileLetter = letter #will be used for texture
        self.tileStackValue = stackVal

class gameRules: 
    def __init__(self, maxHeight, maxLetters, timeLimitOnOff, timeLimit, scoreLimit, size):
        self.maxTileHeight = maxHeight
        self.maxLettersPerPlayer = maxLetters
        self.turnTimeLimitToggle = timeLimitOnOff
        self.turnTimeLimit = timeLimit
        self.maxScore = scoreLimit
        self.boardSize = size # in number of tiles in width (and subsequently height as the board is a square)

    

