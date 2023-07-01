import sys
from .drawings import *
from ai import *
from ai import globals as ai_globals
from game import globals
# Game loop
def run():
    while not globals.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if globals.current_state == IN_MENU:
                # Menu event handling
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if check_button_click(
                            start_game_x,
                            start_game_y,
                            BUTTON_WIDTH,
                            BUTTON_HEIGHT,
                            mouse_pos,
                    ):
                        globals.current_state = IN_GAME
                        globals.PLAYER_PIECE = RED_PIECE
                        globals.AI_PIECE = YELLOW_PIECE

                    elif check_button_click(
                            start_agent_game_x,
                            start_agent_game_y,
                            BUTTON_WIDTH,
                            BUTTON_HEIGHT,
                            mouse_pos,
                    ):
                        globals.current_state = IN_GAME
                        globals.PLAYER_PIECE = YELLOW_PIECE
                        globals.AI_PIECE = RED_PIECE

                    elif check_button_click(
                            creator_x,
                            creator_y,
                            BUTTON_WIDTH,
                            BUTTON_HEIGHT,
                            mouse_pos,
                    ):
                        globals.current_state = IN_CREATOR

                    elif check_button_click(
                            button1_x,
                            settings_y,
                            BUTTON_WIDTH // 3,
                            BUTTON_HEIGHT,
                            mouse_pos,
                        ):
                        globals.settings_button_colors[0] = [GREEN, GREY, GREY]
                        ai_globals.LEVEL = EASY

                    elif check_button_click(
                            button2_x,
                            settings_y,
                            BUTTON_WIDTH // 3,
                            BUTTON_HEIGHT,
                            mouse_pos,
                        ):
                        globals.settings_button_colors[0] = [GREY, GREEN, GREY]
                        ai_globals.LEVEL = MEDIUM

                    elif check_button_click(
                            button3_x,
                            settings_y,
                            BUTTON_WIDTH // 3,
                            BUTTON_HEIGHT,
                            mouse_pos,
                        ):
                        globals.settings_button_colors[0] = [GREY, GREY, GREEN]
                        ai_globals.LEVEL = HARD

                    elif check_button_click(
                            button4_x,
                            settings2_y,
                            BUTTON_WIDTH // 3,
                            BUTTON_HEIGHT,
                            mouse_pos,
                        ):
                        globals.settings_button_colors[1] = [GREEN, GREY, GREY]
                        ai_globals.ALGORITHM = NORMAL_MINIMAX

                    elif check_button_click(
                            button5_x,
                            settings2_y,
                            BUTTON_WIDTH // 3,
                            BUTTON_HEIGHT,
                            mouse_pos,
                        ):
                        globals.settings_button_colors[1] = [GREY, GREEN, GREY]
                        ai_globals.ALGORITHM = ALPHABETA_MINIMAX

                    elif check_button_click(
                            button6_x,
                            settings2_y,
                            BUTTON_WIDTH // 3,
                            BUTTON_HEIGHT,
                            mouse_pos,
                        ):
                        globals.settings_button_colors[1] = [GREY, GREY, GREEN]
                        ai_globals.ALGORITHM = Q_LEARNING

            elif globals.current_state == IN_CREATOR:
                # Creator page event handling
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    back_button_x = MENU_WIDTH // 2 - BUTTON_WIDTH // 2
                    back_button_y = MENU_HEIGHT // 2 + 2 * BUTTON_HEIGHT

                    if check_button_click(
                            back_button_x,
                            back_button_y,
                            BUTTON_WIDTH,
                            BUTTON_HEIGHT,
                            mouse_pos,
                    ):
                        globals.current_state = IN_MENU

            elif globals.current_state == IN_GAME:
                if globals.turn == globals.PLAYER_PIECE:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        posx = event.pos[0]
                        col = int(posx / SQUARE_SIZE)

                        if is_valid_location(globals.board, col):
                            put_piece(globals.board, col, globals.turn)

                            if game_finished(globals.board):
                                globals.current_state = IN_FINISHED_GAME
                                continue

                            draw_board(globals.board)
                            globals.turn = toggled_turn(globals.turn)

                if globals.turn == globals.AI_PIECE:
                    col = agent.run()[0]
                    if is_valid_location(globals.board, col):
                        put_piece(globals.board, col, globals.turn)

                        if game_finished(globals.board):
                            globals.current_state = IN_FINISHED_GAME
                            continue

                        draw_board(globals.board)

                        globals.turn = toggled_turn(globals.turn)

                # if globals.turn == globals.AI_PIECE and ai_globals.ALGORITHM == Q_LEARNING:
                #     agent.run()

        if globals.current_state == IN_MENU:
            draw_menu()

        elif globals.current_state == IN_GAME:
            draw_board(globals.board)

        elif globals.current_state == IN_CREATOR:
            draw_creator_page()

        elif globals.current_state == IN_FINISHED_GAME:
            draw_finished_game(globals.board)