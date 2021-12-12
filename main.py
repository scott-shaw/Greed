# Author: Scott Shaw
# IMPROVE REWARD FUNC
# add multi-threading

import numpy as np
from greed import *
import os
import getch
from randomAgent import *
from circularAgent import *
from qLearningAgent import *
from time import sleep
import argparse
import util
from matplotlib import pyplot as plt
import pandas as pd
from copy import copy, deepcopy

np.random.seed(225)

# Define board and initial position
n = (20,40)
state = np.random.randint(1,10, n)
init = np.random.randint(0,10, (2, 1))
state[init[0][0],init[1][0]] = 0
state_copy = deepcopy(state)
init_copy = deepcopy(init)

# Initialize game
greed_game = Greed(state, (init[0][0],init[1][0]), n)

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--random", action="store_true", help="runs greed using a random agent")
parser.add_argument("-c", "--circular", action="store_true", help="runs greed using a circular agent")
parser.add_argument("-q", "--qlearn", action="store_true", help="runs greed using a q-learning agent")
parser.add_argument('-i', '--iterations', nargs=1, type=int, help='number of iterations of the agent')
parser.add_argument("--no_graphics", action="store_true", help="runs the current agent without graphics")
args = parser.parse_args()
loops = args.iterations[0] if args.iterations else 1

scores = []
q_agent = QLearningAgent(greed_game, 0.999, 0.0005, 1)
epsilon_decay = 0.001
epsilon_initial = 0.5
epsilon_min_bound = 0.01
# Play game with random agent
for i in range(loops):
    if args.random:
        rand_agent = RandomAgent(greed_game)
        while(not greed_game.gameOver()):
            if args.no_graphics:
                rand_agent.takeAction()
            else:
                sleep(0.5)
                greed_game.playGreed()
                rand_agent.takeAction()
                
        if args.no_graphics:
            greed_game.printScore()
        else:
            sleep(0.5)
            greed_game.printState()
        scores.append(greed_game.getScore())

    elif args.circular:
        rand_agent = CircularAgent(greed_game)
        while(not greed_game.gameOver()):
            if args.no_graphics:
                rand_agent.takeAction()
            else:
                sleep(0.5)
                greed_game.playGreed()
                rand_agent.takeAction()

        if args.no_graphics:
            greed_game.printScore()
        else:
            sleep(0.5)
            greed_game.printState()
        scores.append(greed_game.getScore())

    # init q values
    # pick action from current state using e-greedy policy
    # take action
    # update current q value using target reward and target q-value
    elif args.qlearn:
        q_agent.setEpsilon(util.decay(epsilon_decay, i, epsilon_initial, epsilon_min_bound))
        #q_agent.setLearningRate(util.decay(decay, i))
        while(not greed_game.gameOver()):
            action = q_agent.getAction(greed_game)
            old_state = deepcopy(greed_game)
            if args.no_graphics:
                greed_game.takeAction(action)
            else:
                sleep(0.5)
                greed_game.playGreed()
                greed_game.takeAction(action)
            q_agent.update(old_state, action, greed_game, greed_game.getReward(action))
        
        if args.no_graphics:    
            greed_game.printScore()
        else:
            sleep(0.5)
            greed_game.printState()
        scores.append(greed_game.getScore())

    # state = np.random.randint(1,10, n)
    # init = np.random.randint(0,10, (2, 1))
    # state[init[0][0],init[1][0]] = 0
    state = deepcopy(state_copy)
    init = deepcopy(init_copy)


    # Initialize game
    greed_game = Greed(state, (init[0][0],init[1][0]), n)

if loops > 1:
    print("=========================================")
    print("Average Score (%): {}".format(np.mean(scores)))

# Play game with user input
if not args.random and not args.qlearn and not args.circular:
    os.system('cls' if os.name == 'nt' else 'clear')
    while(not greed_game.gameOver()):
        greed_game.playGreed()
        greed_game.takeAction(getch.getch())
        os.system('cls' if os.name == 'nt' else 'clear')
    greed_game.printState()

iterations = np.linspace(0, loops, loops)

plt.plot(scores)
plt.plot(pd.Series(scores).rolling(5).mean())
plt.savefig("mygraph.png")

