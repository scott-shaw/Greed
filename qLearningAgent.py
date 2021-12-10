import numpy as np
import util
import random
from greed import *

np.random.seed(250)

class QLearningAgent:
    
    def __init__(self, state, discount, alpha, epsilon):
        self.discount = discount
        self.alpha = alpha
        self.epsilon = epsilon
        self.weights = util.Counter()
    
    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        return np.dot(self.weights, state.getFeatures(action))

    def computeValueFromQValues(self, state):
        validActions = state.getValidActions(state.getPos())
        if len(validActions) == 0: return 0.0
        return self.getQValue(state, self.getPolicy(state))

    def computeActionFromQValues(self, state):
        validActions = state.getValidActions(state.getPos())
        if len(validActions) == 0: return None
        return validActions[np.argmax([self.getQValue(state, act) for act in validActions])]

    def getAction(self, state):
        validActions = state.getValidActions(state.getPos())
        return random.choice(validActions) if util.flipCoin(self.epsilon) else self.getPolicy(state)

    def update(self, state, action, nextState, reward):
        d = (reward + self.discount * self.getValue(nextState)) - self.getQValue(state, action)
        feat = state.getFeatures(action)
        for f in feat: self.weights[f] += self.alpha * d * feat[f]

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)