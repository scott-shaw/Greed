# mean: 13.922 over 100,000 iterations

import numpy as np
import random

class RandomAgent:
    
    def __init__(self, greedGame):
        self.greedGame = greedGame
        self.actions = self.greedGame.getValidActions(self.greedGame.getPos())
        
    def takeAction(self):
        self.actions = self.greedGame.getValidActions(self.greedGame.getPos())
        a = self.actions[random.randint(0,len(self.actions)-1)]
        self.greedGame.takeAction(a) 

