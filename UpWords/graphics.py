import pyglet
import sys
from UpWords import main
from math import degrees
from pyglet.window import key
from UpWords.main import gameRules
from pyglet import shapes

# ------------ Global Variables ------------
mainWindowHeight = 1024
mainWindowWidth = 720
settingWindowHeight = 640
settingWindowWidth = 640
startWindowHeight = 640
startWindowWidth = 640

# indicates where in the main window the board tiles begin
tilesStartingCoordinateX = 10
tilesStartingCoordinateY = 10

# ----------- Objects and Arrays -------------
# Array of objects for each tile space on the board
boardTiles = []

# creates object with default game rules/settings
defaultRules = gameRules(5, 7, False, 0, 100, 30)

# creates a variable for current rules to be used so that rules used can be modified by setting selectedRules to a new object
selectedRules = defaultRules

# ---------- Windows -------------
# creates starting screen window
startWindow = pyglet.window.Window(startWindowHeight, startWindowWidth, "UpWords", resizable=False)
#creates main window
mainWindow = pyglet.window.Window(mainWindowHeight, mainWindowWidth, "UpWords", resizable=False, visible=False)
#can be set visible when needed with window.set_visible()
#creates settings window
settingsWindow = pyglet.window.Window(settingWindowHeight, settingWindowWidth, "Settings", resizable=False, visible=False)
#can be set visible when needed with window.set_visible()


# ----------- Graphics --------------
# Creating the board
@window.event
def on_draw():
    # calculates appropriate blank tile size by taking total space of the board (window width - gutter space) and dividing by selected board size in tiles
    # this will allow the board tiles to scale as board size is changed
    blankTileSize = (mainWindowWidth - (tilesStartingCoordinateX * 2)) / selectedRules.boardSize
    # draw squares textured with upwords board blank tile based on boardSize from gameRules class
    for x in range(selectedRules.boardSize):
        for y in range(selectedRules.boardSize):
            tile = shapes.Rectangle(x=tilesStartingCoordinateX + (blankTileSize * x), y=tilesStartingCoordinateY + (blankTileSize * x), 
            height=blankTileSize, width=blankTileSize, color=(255, 255, 255))


    # draw border rectangles textured with something

    # draw space for player's current letter tiles in side or bottom bar
