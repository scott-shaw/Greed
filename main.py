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
q_agent = QLearningAgent(greed_game, 0.9, 0.2, 0.05)

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
            pos = greed_game.getPos()
            pos_val = util.stateEncoding(pos,n)
            action_val = q_agent.getAction(pos_val, [util.actionEncoding(x) for x in greed_game.getValidActions(pos)])
            action = util.actionDecoding(action_val)

            #print('chosen action: {}/{}'.format(action_val, action))
            greed_game.takeAction(action)

            new_valid_actions = [util.actionEncoding(x) for x in greed_game.getValidActions(greed_game.getPos())]
            q_agent.update(pos_val, action_val, util.stateEncoding(greed_game.getNextPos(pos,action),n), greed_game.getReward(action), new_valid_actions)
   
        #greed_game.printScore()
        scores.append(greed_game.getScore())

    state = np.random.randint(1,10, n)
    init = np.random.randint(0,10, (2, 1))
    state[init[0][0],init[1][0]] = 0
    # state = state_copy
    # init = init_copy


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

import pandas as pd

plt.plot(scores)
plt.plot(pd.Series(scores).rolling(50).mean())
plt.savefig("mygraph.png")

