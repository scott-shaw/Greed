import numpy as np
import random

np.random.seed(250)

# states encoding
# x = 0 -> 0-39
# x = 1 -> 40-79
# .
# .
# .
# # x = 20 -> 760-799
# 20,40
def stateEncoding(pos, n):
    layer_size = n[1]
    layer = (pos[0]-1) * layer_size
    position = layer + pos[1]
    return position-1

def actionEncoding(action):
    if action == 'q': return 0
    elif action == 'w': return 1
    elif action == 'e': return 2
    elif action == 'a': return 3
    elif action == 'd': return 4
    elif action == 'z': return 5
    elif action == 's': return 6
    elif action == 'c': return 7

def actionDecoding(action):
    if action == 0: return 'q'
    elif action == 1: return 'w'
    elif action == 2: return 'e'
    elif action == 3: return 'a'
    elif action == 4: return 'd'
    elif action == 5: return 'z'
    elif action == 6: return 's'
    elif action == 7: return 'c'

def flipCoin(p):
    r = random.random()
    return r < p
