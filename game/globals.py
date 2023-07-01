from .functions import *
from .constants import *

game_over = False
turn = RED_PIECE
PLAYER_PIECE = RED_PIECE
AI_PIECE = YELLOW_PIECE

board = create_board()

current_state = IN_MENU

settings_button_colors = [[GREY, GREEN, GREY], [GREY, GREEN, GREY]]

MINIMAX_DEPTH = 6
LEVEL = MEDIUM
ALGORITHM = ALPHABETA_MINIMAX
