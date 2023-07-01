import pygame

from .functions import *
from .constants import *

# Game variables
game_over = False
turn = RED_PIECE
PLAYER_PIECE = RED_PIECE
AI_PIECE = YELLOW_PIECE

# Create the game board
board = create_board()

# Initialize game state
current_state = IN_MENU

settings_button_colors = [[GREY, GREEN, GREY], [GREY, GREEN, GREY]]

MINIMAX_DEPTH = 6
LEVEL = MEDIUM
ALGORITHM = ALPHABETA_MINIMAX
