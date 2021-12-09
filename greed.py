import numpy as np
from termcolor import cprint
import getch

# possible features:
# surrounding values
# count of each number on board 0-9

class Greed:
    def __init__(self,s,pos,n):
        self.state = s
        self.pos = pos
        self.n = n
        self.actions = {'q': (-1,-1), 'w': (-1,0), 'e': (-1,1), 'a': (0,-1), 'd': (0,1), 'z': (1,-1), 's': (1,0), 'c': (1,1)}

    def getState(self):
        return self.state

    def getPos(self):
        return self.pos

    def getTotalValue(self):
        return np.sum(self.state)

    # p: position
    # a: action
    def getNextPos(self, p, a):
        if a not in self.getValidActions(p): return p
        x, y = self.actions[a]
        pos = (p[0]+x, p[1]+y)
        val = self.state[(p[0]+x, p[1]+y)]

        return (self.pos[0]+(x*val), self.pos[1]+(y*val))

    # number of tiles removed + number of actions at next state
    def getReward(self, a):
        if a not in self.getValidActions(self.pos): return 0

        next_pos = self.getNextPos(self.pos, a)
        acts_at_next = self.getValidActions(next_pos)

        acts_at_next_next = []
        for act in acts_at_next:
            next_next_pos = self.getNextPos(next_pos, act)
            acts_at_next_next.append(len(self.getValidActions(next_next_pos)))

        if len(acts_at_next) == 0 or np.sum(acts_at_next_next) == 0:
            return -50
        # elif len(acts_at_next) + np.sum(acts_at_next_next) < 10:
        #     return -10
        else:
            return len(acts_at_next) + np.sum(acts_at_next_next)

    # v: x or y position
    # axis: the axis on which v lies -> 0 for x, 1 for y
    def inBounds(self, v, axis):
        return v >= 0 and v < self.n[axis]

    # x, y: binary values which represent the direction of the move
    def isValid(self, x, y, pos):
        if not self.inBounds(pos[0]+x, 0) or not self.inBounds(pos[1]+y, 1): return False
        val = self.state[pos[0]+x, pos[1]+y]
        if val == 0: return False
        if not self.inBounds(pos[0]+(val*x), 0) or not self.inBounds(pos[1]+(val*y), 1): return False
        for i in range(1, val+1):
            if self.state[pos[0]+(i*x), pos[1]+(i*y)] == 0: return False
        return True

    # use binary direction vectors to check validity of moves in every direction
    def getValidActions(self, pos):
        idx = 0
        valid = ['q', 'w', 'e', 'a', 'd', 'z', 's', 'c']
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if i == 0 and j == 0:
                    pass
                else:    
                    if not self.isValid(i, j, pos): 
                        valid.pop(idx)
                    else:
                        idx += 1
        return valid

    # x, y: binary values which represent the direction of the move
    def move(self, x, y):
        val = self.state[self.pos[0]+x, self.pos[1]+y]
        for i in range(val+1):
            self.state[self.pos[0]+(i*x), self.pos[1]+(i*y)] = 0
        self.pos = (self.pos[0]+(val*x), self.pos[1]+(val*y)) 

    # a: character value which represents an action
    # possible actions: w, s, a, d, q, c, e, z
    def takeAction(self, a): 
        if a not in self.getValidActions(self.pos): return
        if a == 'w': self.move(-1, 0)
        elif a == 's': self.move(1, 0)
        elif a == 'a': self.move(0, -1)
        elif a == 'd': self.move(0, 1)
        elif a == 'q': self.move(-1, -1)
        elif a == 'c': self.move(1, 1)
        elif a == 'e': self.move(-1, 1)
        elif a == 'z': self.move(1, -1)

    def gameOver(self):
        return True if not self.getValidActions(self.pos) else False
        
    def getScore(self):
        return np.count_nonzero(self.state==0) / (self.n[0] * self.n[1]) * 100

    def printScore(self):
        print('Score (%): {}'.format(self.getScore()))

    def printState(self):
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if i == self.pos[0] and j == self.pos[1]:
                    cprint('@ ', 'cyan', end='') 
                elif self.state[i,j] == 0:
                    print('  ', end='')
                else:
                    cprint('{} '.format(self.state[i,j]), 'red', end='')
            print()
        if not self.gameOver():
            print('===========================')
        else:
            print('\nGame Over!')
            print('Score (%): {}\n'.format(self.getScore()))

    def playGreed(self):
        print('Make a move. Current state:')
        self.printState()
        print('Available Actions: {}'.format(self.getValidActions(self.pos)))
        #self.takeAction(getch.getch())

