import math

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
SIZE = (WIDTH, HEIGHT)
BLACK = (30, 30, 30)
RED = (219, 0, 0)
YELLOW = (255, 204, 0)
WHITE = (245, 245, 245)
GREY = (100, 100, 100)
GREEN = (0, 150, 0)
MENU_BACKGROUND_COLOR = BLACK
GAME_BACKGROUND_COLOR = BLACK
GAME_SIDES_COLOR = GREY

IN_MENU = "MENU"
IN_GAME = "GAME"
IN_CREATOR = "CREATOR"
IN_FINISHED_GAME = "FINISHED_GAME"

RED_PIECE = "RED_PIECE"
YELLOW_PIECE = "YELLOW_PIECE"
EMPTY_PIECE = "EMPTY_PIECE"

RED_WON = "RED_WON"
YELLOW_WON = "YELLO_WON"
DRAW = "DRAW"
PENDING = "PENDING"

MENU_WIDTH = WIDTH
MENU_HEIGHT = HEIGHT
BUTTON_WIDTH = 400
BUTTON_HEIGHT = 50
MENU_PADDING = 15

start_game_x = MENU_WIDTH // 2 - BUTTON_WIDTH // 2
start_game_y = MENU_HEIGHT // 2 - BUTTON_HEIGHT // 2 + 2 * BUTTON_HEIGHT + MENU_PADDING
start_agent_game_x = MENU_WIDTH // 2 - BUTTON_WIDTH // 2
start_agent_game_y = start_game_y + BUTTON_HEIGHT + MENU_PADDING
creator_x = MENU_WIDTH // 2 - BUTTON_WIDTH // 2
creator_y = start_agent_game_y + BUTTON_HEIGHT + MENU_PADDING

button_padding = MENU_WIDTH // 2 - BUTTON_WIDTH // 2

button_width = BUTTON_WIDTH // 3
button_height = BUTTON_HEIGHT
button1_x = button_padding
button2_x = button_width + button_padding
button3_x = button_width * 2 + button_padding
button4_x = button_padding
button5_x = button_width + button_padding
button6_x = button_width * 2 + button_padding
settings_y = MENU_HEIGHT // 2 - BUTTON_HEIGHT // 2 - MENU_PADDING
settings2_y = settings_y + button_height + MENU_PADDING

INFINITY = math.inf
NEGATIVE_INFINITY = -INFINITY

# Levels
EASY = "EASY"
MEDIUM = "MEDIUM"
HARD = "HARD"

# Algorithm
NORMAL_MINIMAX = "NORMAL_MINIMAX"
ALPHABETA_MINIMAX = "ALPHABETA_MINIMAX"
Q_LEARNING = "Q_LEARNING"