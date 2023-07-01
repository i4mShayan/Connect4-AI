from game.functions import *

def score_line(line, piece):
    opponent_piece = opponent(piece)
    score = 0

    if line.count(piece) == 3 and line.count(EMPTY_PIECE) == 1:
        score += 10
    elif line.count(piece) == 2 and line.count(EMPTY_PIECE) == 2:
        score += 5
    elif line.count(opponent_piece) == 3 and line.count(EMPTY_PIECE) == 1:
        score -= 10

    return score

def get_col(board, col):
    return [row[col] for row in board]

def vertical_line(board, r, c):
    return [board[r][c] for r in range(r, r + 4)]

def score_horizontal_lines(board, piece):
    score = 0
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            line = board[row][col:col + 4]
            score += score_line(line, piece)
    return score

def score_vertical_lines(board, piece):
    score = 0
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT):
            score += score_line(vertical_line(board, row, col), piece)
    return score

def score_column(board, piece, col, score):
    column = get_col(board, col)
    center_count = column.count(piece)
    return center_count * score

def score_center_columns(board, piece):
    center_column = COLUMN_COUNT // 2
    return score_column(board, piece, center_column, 5) + score_column(board, piece, center_column-1, 2) + score_column(board, piece, center_column+1, 2)

def score_state(board, piece):
    return score_center_columns(board, piece) + score_vertical_lines(board, piece) + score_horizontal_lines(board, piece)
