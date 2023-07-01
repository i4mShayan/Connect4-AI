import pygame

from .constants import *
from . import globals
from .functions import *

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect 4")
font = pygame.font.Font(None, 36)

def draw_board(board):
    screen.fill(GAME_BACKGROUND_COLOR)
    turn_text = font.render(f"Turn: {player_name(globals.turn, globals.AI_PIECE)}", True, player_color(globals.turn))
    turn_x = WIDTH // 2 - turn_text.get_width() // 2
    turn_y = SQUARE_SIZE // 2 - turn_text.get_height() // 2
    screen.blit(turn_text, (turn_x, turn_y))

    draw_game_board(board)

def draw_circle(screen, color, c, r, height):
    pygame.draw.circle(
        screen,
        color,
        (
            int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
            height - int(r * SQUARE_SIZE + SQUARE_SIZE / 2),
        ),
        RADIUS,
    )

def draw_game_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(
                screen,
                GAME_SIDES_COLOR,
                (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )
            pygame.draw.circle(
                screen,
                GAME_BACKGROUND_COLOR,
                (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                    int((r + 1) * SQUARE_SIZE + SQUARE_SIZE / 2),
                ),
                RADIUS,
            )

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == RED_PIECE:
                draw_circle(screen, RED, c, r, HEIGHT)
            elif board[r][c] == YELLOW_PIECE:
                draw_circle(screen, YELLOW, c, r, HEIGHT)

    pygame.display.update()



def draw_menu():
    screen.fill(MENU_BACKGROUND_COLOR)
    background_image = pygame.image.load("assets/logo.png")
    screen.blit(background_image, (WIDTH // 10, 0))

    draw_settings()

    draw_button(
        start_game_x,
        start_game_y,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
        "Start game with playing first",
        text_color=RED,
    )

    draw_button(
        start_agent_game_x,
        start_agent_game_y,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
        "Start game with AI first",
        text_color=YELLOW,
    )

    draw_button(
        creator_x,
        creator_y,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
        "Creator",
    )

    pygame.display.update()


def draw_creator_page():
    screen.fill(MENU_BACKGROUND_COLOR)
    creator_text = font.render("Creator: Github.com/i4mShayan", True, WHITE)
    text_x = MENU_WIDTH // 2 - creator_text.get_width() // 2
    text_y = MENU_HEIGHT // 2 - creator_text.get_height() // 2
    screen.blit(creator_text, (text_x, text_y))

    draw_button(
        MENU_WIDTH // 2 - BUTTON_WIDTH // 2,
        MENU_HEIGHT // 2 + 2 * BUTTON_HEIGHT,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
        "Back",
    )

    pygame.display.update()


def draw_finished_game(board):
    screen.fill(GAME_BACKGROUND_COLOR)
    if no_move_remaining(board):
        winner_text = font.render(f"Draw!", True, WHITE)
    else:
        winner_text = font.render(f"{player_name(globals.turn, globals.AI_PIECE)} WON!", True, player_color(globals.turn))

    winner_x = WIDTH // 2 - winner_text.get_width() // 2
    winner_y = SQUARE_SIZE // 2 - winner_text.get_height() // 2
    screen.blit(winner_text, (winner_x, winner_y))
    draw_game_board(board)
    pygame.display.update()


def draw_button(x, y, width, height, text, button_color=BLACK, text_color=WHITE, border_color=WHITE, border_width=2, border_radius=20):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, button_color, button_rect, border_radius=border_radius)
    pygame.draw.rect(screen, border_color, button_rect, width=border_width, border_radius=border_radius)
    button_text = font.render(text, True, text_color)
    text_x = x + width // 2 - button_text.get_width() // 2
    text_y = y + height // 2 - button_text.get_height() // 2
    screen.blit(button_text, (text_x, text_y))

def draw_settings(border_radius=20):
    button1_rect = pygame.Rect(button1_x, settings_y, button_width, button_height)
    button2_rect = pygame.Rect(button2_x, settings_y, button_width, button_height)
    button3_rect = pygame.Rect(button3_x, settings_y, button_width, button_height)
    button4_rect = pygame.Rect(button4_x, settings2_y, button_width, button_height)
    button5_rect = pygame.Rect(button5_x, settings2_y, button_width, button_height)
    button6_rect = pygame.Rect(button6_x, settings2_y, button_width, button_height)

    level_border_rect = pygame.Rect(button1_x, settings_y, button_width * 3, button_height)
    algorithm_border_rect = pygame.Rect(button4_x, settings_y * 2 + button_height, button_width * 3, button_height)

    pygame.draw.rect(screen, globals.settings_button_colors[0][0], button1_rect, border_top_left_radius=border_radius, border_bottom_left_radius=border_radius)
    pygame.draw.rect(screen, globals.settings_button_colors[0][1], button2_rect)
    pygame.draw.rect(screen, globals.settings_button_colors[0][2], button3_rect, border_top_right_radius=border_radius,
                     border_bottom_right_radius=border_radius)

    pygame.draw.rect(screen, globals.settings_button_colors[1][0], button4_rect, border_top_left_radius=border_radius, border_bottom_left_radius=border_radius)
    pygame.draw.rect(screen, globals.settings_button_colors[1][1], button5_rect)
    pygame.draw.rect(screen, globals.settings_button_colors[1][2], button6_rect, border_top_right_radius=border_radius,
                     border_bottom_right_radius=border_radius)

    text1 = font.render("Easy", True, WHITE)
    text2 = font.render("Medium", True, WHITE)
    text3 = font.render("Hard", True, WHITE)
    text4 = font.render("Normal", True, WHITE)
    text5 = font.render("AlphaBeta", True, WHITE)
    text6 = font.render("Q Learn", True, WHITE)
    text1_pos = text1.get_rect(center=(button1_rect.centerx, button1_rect.centery))
    text2_pos = text2.get_rect(center=(button2_rect.centerx, button2_rect.centery))
    text3_pos = text3.get_rect(center=(button3_rect.centerx, button3_rect.centery))
    text4_pos = text4.get_rect(center=(button4_rect.centerx, button4_rect.centery))
    text5_pos = text5.get_rect(center=(button5_rect.centerx, button5_rect.centery))
    text6_pos = text6.get_rect(center=(button6_rect.centerx, button6_rect.centery))
    screen.blit(text1, text1_pos)
    screen.blit(text2, text2_pos)
    screen.blit(text3, text3_pos)
    screen.blit(text4, text4_pos)
    screen.blit(text5, text5_pos)
    screen.blit(text6, text6_pos)

