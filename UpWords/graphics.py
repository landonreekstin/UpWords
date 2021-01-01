import pyglet
import sys
from UpWords import main
from math import degrees
from pyglet.window import key
from UpWords.main import gameRules

# Array of objects for each tile space on the board
boardTiles = []

# creates object with default game rules/settings
defaultRules = gameRules(5, 7, False, 0, 100, 30)

# creates a variable for current rules to be used so that rules used can be modified by setting selectedRules to a new object
selectedRules = defaultRules



#creates main window
mainWindow = pyglet.window.Window(1024, 720, "UpWords", resizable=False)

#creates settings window
settingsWindow = pyglet.window.Window(640, 640, "Settings", resizable=False, visible=False)
#can be set visible when needed with window.set_visible()

# Creating the board
@window.event
def on_draw():
    # draw squares textured with upwords board blank tile based on boardSize from gameRules class
    for x in range(selectedRules.boardSize):
        

    # draw border rectangles textured with something

    # draw space for player's current letter tiles in side or bottom bar
