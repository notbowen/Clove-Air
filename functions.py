# functions.py
# Storage of global functions

# Libraries
import random

# Functions
async def generateRandomColor():
    randomColor = lambda: random.randint(0,255)
    color = int("0x%02X%02X%02X" % (randomColor(),randomColor(),randomColor()), 16)
    return color