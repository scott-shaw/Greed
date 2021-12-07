# Author: Scott Shaw

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
parser.add_argument("-r", "--random", action="store_true", help="runs greed using a random agent")
parser.add_argument("-q", "--qlearn", action="store_true", help="runs greed using a q-learning agent")
parser.add_argument('-i', '--iterations', nargs=1, type=int, help='number of iterations of the agent')
parser.add_argument("--no_graphics", action="store_true", help="runs the current agent without graphics")
args = parser.parse_args()

loops = args.iterations[0] if args.iterations else 1

scores = []

# Play game with random agent
for i in range(loops):
    if args.random:
        rand_agent = RandomAgent(greed_game)
        while(not greed_game.gameOver()):
            if args.no_graphics:
                rand_agent.takeAction()
            else:
                greed_game.playGreed()
                rand_agent.takeAction()
                sleep(0.5)
        if args.no_graphics:
            greed_game.printScore()
        else:
            greed_game.printState()
        scores.append(greed_game.getScore())

    # Play game with user input
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        while(not greed_game.gameOver()):
            greed_game.playGreed()
            greed_game.takeAction(getch.getch())
            os.system('cls' if os.name == 'nt' else 'clear')
        greed_game.printState()


    state = np.random.randint(1,10, n)
    init = np.random.randint(0,10, (2, 1))
    state[init[0][0],init[1][0]] = 0

    # Initialize game
    greed_game = Greed(state, (init[0][0],init[1][0]), n)

print("=========================================")
print("Average Score (%): {}".format(np.mean(scores)))
