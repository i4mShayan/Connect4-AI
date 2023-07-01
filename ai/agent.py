import copy
import game
from game.constants import *
from ai import alpha_beta_minimax, normal_minimax, normal_minimax_with_transposition_table, q_learning
from game import globals

q_agent = q_learning.QLearningAgent()

def run():
    if globals.ALGORITHM == NORMAL_MINIMAX:
        if globals.LEVEL == EASY:
            globals.MINIMAX_DEPTH = 3
        elif globals.LEVEL == MEDIUM:
            globals.MINIMAX_DEPTH = 6
        elif globals.LEVEL == HARD:
            globals.MINIMAX_DEPTH = 7
        return normal_minimax_with_transposition_table(copy.deepcopy(game.globals.board))
        # return normal_minimax(copy.deepcopy(game.globals.board))

    elif globals.ALGORITHM == ALPHABETA_MINIMAX:
        if globals.LEVEL == EASY:
            globals.MINIMAX_DEPTH = 3
        elif globals.LEVEL == MEDIUM:
            globals.MINIMAX_DEPTH = 6
        elif globals.LEVEL == HARD:
            globals.MINIMAX_DEPTH = 7
        return alpha_beta_minimax(copy.deepcopy(game.globals.board))

    elif globals.ALGORITHM == Q_LEARNING:
        iteration_count = 0
        if globals.LEVEL == EASY:
            iteration_count = 1e3
        elif globals.LEVEL == MEDIUM:
            iteration_count = 1e4
        elif globals.LEVEL == HARD:
            iteration_count = 1e6
        if not q_agent.is_trained:
            q_agent.train(iteration_count=int(iteration_count))
        return q_agent.get_action(copy.deepcopy(game.globals.board)), 0




