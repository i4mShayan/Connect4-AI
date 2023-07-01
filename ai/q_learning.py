import random
from game.functions import *
from game import globals

class QLearningAgent:
    def __init__(self, epsilon=0.5, alpha=0.5, gamma=0.5, is_trained=False):
        self.q_values = {}
        self.epsilon = epsilon  # Exploration rate
        self.alpha = alpha      # Learning rate
        self.gamma = gamma      # Discount factor
        self.is_trained = is_trained

    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, COLUMN_COUNT-1)
        else:
            state_tuple = tuple(map(tuple, state))
            return max(range(COLUMN_COUNT), key=lambda col: self.q_values.get((state_tuple, col), 0))

    def update_q_value(self, state, action, next_state, reward):
        state_tuple = tuple(map(tuple, state))
        next_state_tuple = tuple(map(tuple, next_state))

        current_q = self.q_values.get((state_tuple, action), 0)

        max_next_q = max(self.q_values.get((next_state_tuple, next_action), 0) for next_action in range(COLUMN_COUNT))

        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)

        self.q_values[(state_tuple, action)] = new_q


def train_agent(agent, iteration_count):
    agent.is_trained = False
    board = create_board()

    for i in range(iteration_count):

        while game_state(board) == globals.PENDING:
            action = agent.get_action(board)

            if not is_valid_location(board, action):
                continue

            put_piece(board, action, globals.AI_PIECE)
            next_state = board

            if is_a_win(board, globals.AI_PIECE):
                reward = 1000
            elif is_a_win(board, globals.PLAYER_PIECE):
                reward = -1000
            else:
                reward = 0

            agent.update_q_value(board, action, next_state, reward)

        board = create_board()
        globals.turn = toggled_turn(globals.turn)
    agent.is_trained = True
