import copy
import random
from game.functions import *
from game import globals

class QLearningAgent:
    def __init__(self):
        self.q_table = {}
        self.is_trained = False
        self.epsilon = 0.5  # Exploration rate
        self.alpha = 0.5  # Learning rate
        self.gamma = 0.5  # Discount factor

    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, COLUMN_COUNT-1)
        else:
            state_tuple = tuple(map(tuple, state))
            return max(range(COLUMN_COUNT), key=lambda col: self.q_table.get((state_tuple, col), 0))

    def update_q(self, state, action, next_state, reward):
        state_tuple = tuple(map(tuple, state))
        next_state_tuple = tuple(map(tuple, next_state))

        current_q = self.q_table.get((state_tuple, action), 0)

        max_next_q = max(self.q_table.get((next_state_tuple, next_action), 0) for next_action in range(COLUMN_COUNT))

        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)

        self.q_table[(state_tuple, action)] = new_q

    def train(self, iteration_count):
        self.is_trained = False
        board = create_board()

        for i in range(iteration_count):
            while game_state(board) == globals.PENDING:
                action = self.get_action(board)

                if not is_valid_move(board, action):
                    continue

                before_board = copy.deepcopy(board)
                put_piece(board, action, globals.AI_PIECE)

                if is_a_win(board, globals.AI_PIECE):
                    reward = 1000
                elif is_a_win(board, globals.PLAYER_PIECE):
                    reward = -1000
                else:
                    reward = 0

                self.update_q(before_board, action, board, reward)

            board = create_board()
            globals.turn = toggled_turn(globals.turn)
        self.is_trained = True
