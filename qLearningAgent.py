import numpy as np
import util
import random

np.random.seed(250)

class QLearningAgent:
    
    def __init__(self, state, discount, alpha, epsilon):
        self.state = state
        self.discount = discount
        self.alpha = alpha
        self.epsilon = epsilon
        self.q = np.zeros((800, 8))
    
    def getQValue(self, state, action):
        return self.q[state, action]

    def computeValueFromQValues(self, state, validActions):
        if len(validActions) == 0: return 0.0
        return self.getQValue(state, self.getPolicy(state, validActions))

    def computeActionFromQValues(self, state, validActions):
        if len(validActions) == 0: return None
        return validActions[np.argmax([self.getQValue(state, act) for act in validActions])]

    def getAction(self, state, validActions):
        return random.choice(validActions) if util.flipCoin(self.epsilon) else self.getPolicy(state, validActions)

    def update(self, state, action, nextState, reward, nextValidActions):
        q = self.getQValue(state, action)
        self.q[state, action] = q + self.alpha * (reward + self.discount * self.getValue(nextState, nextValidActions) - q)

    def getPolicy(self, state, validActions):
        return self.computeActionFromQValues(state, validActions)

    def getValue(self, state, validActions):
        return self.computeValueFromQValues(state, validActions)