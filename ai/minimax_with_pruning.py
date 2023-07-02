import copy
from ai.heuristic import *
from game.constants import *
from game import globals

def alpha_beta_minimax(board, depth=0, alpha=-INFINITY, beta=INFINITY, max_player=True):
    finish_of_game = game_finished(board)
    available_moves = get_available_moves(board)

    if finish_of_game:
        if is_a_win(board, globals.AI_PIECE):
            return None, INFINITY
        elif is_a_win(board, globals.PLAYER_PIECE):
            return None, -INFINITY
        else:
            return 0, 0
    if depth == globals.MINIMAX_DEPTH:
        return None, score_state(board, globals.AI_PIECE)

    if max_player:
        best_score = -INFINITY
        best_col = available_moves[0]

        for col in available_moves:
            board_copy = copy.deepcopy(board)
            put_piece(board_copy, col, globals.AI_PIECE)

            score = alpha_beta_minimax(board_copy, depth + 1, alpha, beta, False)[1]

            if score > best_score:
                best_score = score
                best_col = col

            alpha = max(best_score, alpha)

            if alpha >= beta:
                break

        return best_col, best_score

    else:
        best_score = INFINITY
        best_col = available_moves[0]

        for col in available_moves:
            board_copy = copy.deepcopy(board)
            put_piece(board_copy, col, globals.PLAYER_PIECE)

            score = alpha_beta_minimax(board_copy, depth + 1, alpha, beta, True)[1]

            if score < best_score:
                best_score = score
                best_col = col

            beta = min(best_score, beta)

            if alpha >= beta:
                break

        return best_col, best_score
