import numpy as np
import random

class CircularAgent:
    
    def __init__(self, greedGame):
        self.greedGame = greedGame
        self.actions = self.greedGame.getValidActions(greedGame.getPos())
        self.current_action = 'w'
        self.action_order = ['w', 'd', 's', 'a', 'e', 'c', 'z', 'q']
        
    def takeAction(self):
        self.actions = self.greedGame.getValidActions(self.greedGame.getPos())

        if self.current_action in self.actions:
            self.greedGame.takeAction(self.current_action)
        else:
            idx = self.action_order.index(self.current_action)

            while self.current_action not in self.actions:
                if idx >= 7:
                    idx = 0
                else: 
                    idx += 1
                self.current_action = self.action_order[idx]
            
            self.greedGame.takeAction(self.current_action)


