import copy
from ai.heuristic import *
from game.constants import *
from game import globals

def normal_minimax_with_transposition_table(board, depth=0, max_play=True, transposition_table={}):

    finish_of_game = game_finished(board)

    if finish_of_game:
        if is_a_win(board, globals.AI_PIECE):
            return 0, INFINITY
        elif is_a_win(board, globals.PLAYER_PIECE):
            return 0, -INFINITY
        else:
            return 0, 0
    if depth == globals.MINIMAX_DEPTH:
        return None, score_state(board, globals.AI_PIECE)

    available_moves = get_available_moves(board)

    if max_play:
        best_score = -INFINITY
        best_col = available_moves[0]

        for col in available_moves:
            board_copy = copy.deepcopy(board)
            put_piece(board_copy, col, globals.AI_PIECE)

            board_key = tuple(map(tuple, board_copy))

            if board_key in transposition_table:
                score = transposition_table[board_key]
            else:
                score = normal_minimax_with_transposition_table(board_copy, depth + 1, False, transposition_table)[1]
                transposition_table[board_key] = score

            if score > best_score:
                best_score = score
                best_col = col

        return best_col, best_score

    else:
        best_score = INFINITY
        best_col = available_moves[0]

        for col in available_moves:
            board_copy = copy.deepcopy(board)
            put_piece(board_copy, col, globals.PLAYER_PIECE)

            board_key = tuple(map(tuple, board_copy))

            if board_key in transposition_table:
                score = transposition_table[board_key]
            else:
                score = normal_minimax_with_transposition_table(board_copy, depth + 1, True, transposition_table)[1]
                transposition_table[board_key] = score

            if score < best_score:
                best_score = score
                best_col = col

        return best_col, best_score

def normal_minimax(board, depth=globals.MINIMAX_DEPTH, max_play=True):

    finish_of_game = game_finished(board)

    if finish_of_game:
        if is_a_win(board, globals.AI_PIECE):
            return None, INFINITY
        elif is_a_win(board, globals.PLAYER_PIECE):
            return None, -INFINITY
        else:
            return None, 0
    if depth == 0:
        return None, score_state(board, globals.AI_PIECE)

    available_moves = get_available_moves(board)

    if max_play:
        best_score = -INFINITY
        best_col = available_moves[0]

        for col in available_moves:
            row = next_available_row(board, col)
            board_copy = copy.deepcopy(board)
            put_piece(board_copy, row, col, globals.AI_PIECE)

            score = normal_minimax(board_copy, depth - 1, False)[1]

            if score > best_score:
                best_score = score
                best_col = col

        return best_col, best_score

    else:
        best_score = INFINITY
        best_col = available_moves[0]

        for col in available_moves:
            row = next_available_row(board, col)
            board_copy = copy.deepcopy(board)
            put_piece(board_copy, row, col, globals.PLAYER_PIECE)

            column, score = normal_minimax(board_copy, depth - 1, True)

            if score < best_score:
                best_score = score
                best_col = column

        return best_col, best_score
