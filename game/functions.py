from .constants import *

def create_board():
    board = [[EMPTY_PIECE] * COLUMN_COUNT for _ in range(ROW_COUNT)]
    return board


# def put_piece(board, row, col, piece):
#     board[row][col] = piece


def put_piece(board, col, piece):
    row = next_available_row(board, col)
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == EMPTY_PIECE


def next_available_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY_PIECE:
            return r


def is_a_win(board, piece):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ):
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ):
                return True

def get_available_moves(board):
    valid_locations = []
    for c in range(COLUMN_COUNT):
        if is_valid_location(board, c):
            valid_locations.append(c)
    return valid_locations

def no_move_remaining(board):
    return len(get_available_moves(board)) == 0

def game_state(board):
    if is_a_win(board, 1):
        return RED_WON
    elif is_a_win(board, 2):
        return YELLOW_WON
    elif no_move_remaining(board):
        return DRAW
    else:
        return PENDING


def game_finished(board):
    return is_a_win(board, RED_PIECE) or is_a_win(board, YELLOW_PIECE) or no_move_remaining(board)

def player_name(turn, AI_PIECE):
    # name = "Yellow" if turn == YELLOW_PIECE else "Red"
    # name += " " + ("(AI)" if turn == AI_PIECE else "(YOU)")
    name = "AI" if turn == AI_PIECE else "YOU"
    return name

def player_color(turn):
    return YELLOW if turn == YELLOW_PIECE else RED

def check_button_click(x, y, width, height, pos):
    mouse_x, mouse_y = pos
    return x <= mouse_x <= x + width and y <= mouse_y <= y + height

def toggled_turn(turn):
    if turn == YELLOW_PIECE:
        return RED_PIECE
    else:
        return YELLOW_PIECE

def opponent(piece):
    return toggled_turn(piece)
