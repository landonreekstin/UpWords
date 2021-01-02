import pyglet
import sys
from math import degrees
from pyglet.window import key
#import UpWords.main
#from UpWords.main import gameRules
from pyglet import shapes
from pyglet.gl import GL_LINES, glBegin, glEnd, glVertex3f, glColor4f

# for testing
# set as import later
# ------- Classes from main.py -------------
class player:
    def __init__(self, name, score, turn):
        self.playerName = name
        self.playerScore = score
        self.playerTurnNo = turn
        self.playerLetterInventory = []


class tile: 
    def __init__(self, tileX, tileY, height, width, color, letter, stackVal):
        self.tileCoordinateX = tileX
        self.tileCoordinateY = tileY
        self.tileHeight = height
        self.tileWidth = width
        self.tileColor = color
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

# ------------ Global Variables ------------
mainWindowHeight = 1024
mainWindowWidth = 720
settingWindowHeight = 640
settingWindowWidth = 640
startWindowHeight = 640
startWindowWidth = 640

# indicates where in the main window the board tiles begin
tilesStartingCoordinateX = 5
tilesStartingCoordinateY = 5
tileSpaceGap = 5

# ----------- Objects and Arrays -------------
# Array of objects for each letter tile on the board
tileArray = []

# creates object with default game rules/settings
defaultRules = gameRules(5, 7, False, 0, 100, 10)

# creates a variable for current rules to be used so that rules used can be modified by setting selectedRules to a new object
selectedRules = defaultRules

# ---------- Windows -------------
# creates starting screen window
startWindow = pyglet.window.Window(startWindowHeight, startWindowWidth, "Main Menu", resizable=False)
#creates main window
mainWindow = pyglet.window.Window(mainWindowHeight, mainWindowWidth, "UpWords", resizable=False, visible=True)
#can be set visible when needed with window.set_visible()
#creates settings window
settingsWindow = pyglet.window.Window(settingWindowHeight, settingWindowWidth, "Settings", resizable=False, visible=False)
#can be set visible when needed with window.set_visible()


# ----------- Graphics --------------
# Creating the board
batch = pyglet.graphics.Batch()
# calculates appropriate blank tile size by taking total space of the board (window width - gutter space) and dividing by selected board size in tiles
# this will allow the board tiles to scale as board size is changed
blankTileSize = (mainWindowWidth - (tilesStartingCoordinateX * 2)) / selectedRules.boardSize
# foces blankTileSize to be an int
blankTileSize = int(blankTileSize)
# create tile objects with properties from current game rules. Game rules must be set before the game is created. Default rules are created if none are set by user
# add tile objects to tileArray
for x in range(selectedRules.boardSize):
    for y in range(selectedRules.boardSize):
        blankTile = tile(tilesStartingCoordinateX + (blankTileSize * x) + tileSpaceGap, 
        tilesStartingCoordinateY + (blankTileSize * y) + tileSpaceGap, blankTileSize, blankTileSize, (255, 0, 0), "blank", 0)
        tileArray.append(blankTile)

@mainWindow.event
def on_draw():
    mainWindow.clear()
    
    # convert tile objects into pyglet squares
    for tiles in range(len(tileArray)):
        square = shapes.Rectangle(tileArray[tiles].tileCoordinateX, tileArray[tiles].tileCoordinateY, tileArray[tiles].tileHeight, tileArray[tiles].tileWidth,
        tileArray[tiles].tileColor, batch=batch)
        square.draw()

    # draw border rectangles textured with something

    # draw space for player's current letter tiles in side or bottom bar


def update(dt):
    pass


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()
