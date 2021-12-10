# Author: Scott Shaw
# add circular agent?
# 
# 
# CHECK WITH NOTES TO SEE IF PROCESS IS CORRECT
# APPROX Q LEARNING? -> I think this is the answer (I need to redefine states)
# IMPROVE REWARD FUNC

import numpy as np
from greed import *
import os
import getch
from randomAgent import *
from qLearningAgent import *
from time import sleep
import argparse
import util
from matplotlib import pyplot as plt
import pandas as pd
from copy import copy, deepcopy

np.random.seed(250)

# Define board and initial position
n = (20,40)
state = np.random.randint(1,10, n)
init = np.random.randint(0,10, (2, 1))
state[init[0][0],init[1][0]] = 0
state_copy = state.copy()
init_copy = init.copy()

# Initialize game
greed_game = Greed(state, (init[0][0],init[1][0]), n)

parser = argparse.ArgumentParser()
#group = parser.add_mutually_exclusive_group()
parser.add_argument("-r", "--random", action="store_true", help="runs greed using a random agent")
parser.add_argument("-q", "--qlearn", action="store_true", help="runs greed using a q-learning agent")
parser.add_argument('-i', '--iterations', nargs=1, type=int, help='number of iterations of the agent')
parser.add_argument("--no_graphics", action="store_true", help="runs the current agent without graphics")
args = parser.parse_args()
loops = args.iterations[0] if args.iterations else 1

scores = []
q_agent = QLearningAgent(greed_game, 0.8, 0.1, 0.05)

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

    # init q values
    # pick action from current state using e-greedy policy
    # take action
    # update current q value using target reward and target q-value
    elif args.qlearn:
        while(not greed_game.gameOver()):
            action = q_agent.getAction(greed_game)
            #action = util.actionDecoding(action_val)
            old_state = deepcopy(greed_game)

            greed_game.takeAction(action)
            q_agent.update(old_state, action, greed_game, greed_game.getReward(action))
   
        if i < 50:
            greed_game.printScore()
        scores.append(greed_game.getScore())

    # state = np.random.randint(1,10, n)
    # init = np.random.randint(0,10, (2, 1))
    # state[init[0][0],init[1][0]] = 0
    state = state_copy
    init = init_copy


    # Initialize game
    greed_game = Greed(state, (init[0][0],init[1][0]), n)

if loops > 1:
    print("=========================================")
    print("Average Score (%): {}".format(np.mean(scores)))

# Play game with user input
if not args.random and not args.qlearn:
    os.system('cls' if os.name == 'nt' else 'clear')
    while(not greed_game.gameOver()):
        greed_game.playGreed()
        greed_game.takeAction(getch.getch())
        os.system('cls' if os.name == 'nt' else 'clear')
    greed_game.printState()

iterations = np.linspace(0, loops, loops)

plt.plot(scores)
plt.plot(pd.Series(scores).rolling(50).mean())
plt.savefig("mygraph.png")

