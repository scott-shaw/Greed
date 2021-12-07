# Author: Scott Shaw
# Requirements
# - numpy
# - termcolor
# - getch

import numpy as np
from greed import *
import os
import getch
from randomAgent import *
from time import sleep
import argparse

np.random.seed(250)

# Define board and initial position
n = (20,40)
state = np.random.randint(1,10, n)
init = np.random.randint(0,10, (2, 1))
state[init[0][0],init[1][0]] = 0

# Initialize game
greed_game = Greed(state, (init[0][0],init[1][0]), n)

parser = argparse.ArgumentParser()
parser.add_argument("--random", action="store_true", help="runs greed using a random agent")
args = parser.parse_args()

# Play game with random agent
if args.random:
    rand_agent = RandomAgent(greed_game)
    while(not greed_game.gameOver()):
        greed_game.playGreed()
        rand_agent.takeAction()
        sleep(0.5)
    greed_game.printState()


# Play game with user input
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    while(not greed_game.gameOver()):
        greed_game.playGreed()
        greed_game.takeAction(getch.getch())
        os.system('cls' if os.name == 'nt' else 'clear')
    greed_game.printState()
