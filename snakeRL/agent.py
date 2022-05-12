
#imprt libraries
import torch
import random
import numpy as np
from collections import deque
from game import SnakeGameAI, Direction, Point

#Parameters
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_maes = 0
        self.epsilon = 0 #randomness
        self.gamma = 0 #discount rate
        self.memory = deque(maxlen = MAX_MEMORY)    #popleft

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self):
        pass

    def get_action(self, state):
        pass

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        #get the old states
        state_old = agent.get_state(game)

        #get the move
        final_move = agent.get_action(state_old)

        #perform move and get the new state
        


if __name__ == '__main__':
    train()