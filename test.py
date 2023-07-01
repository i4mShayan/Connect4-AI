import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Selectable Options")

# Define colors
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

# Define button dimensions
button_width = (screen_width - 40) // 3  # Adjusted for 3 buttons without padding
button_height = 100
button_padding = 0  # Set padding to 0

# Store button colors

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Check level options
            if button1_rect.collidepoint(mouse_pos):
                button_colors[0] = [GREEN, GRAY, GRAY]
                print("Level: Easy")
            elif button2_rect.collidepoint(mouse_pos):
                button_colors[0] = [GRAY, GREEN, GRAY]
                print("Level: Medium")
            elif button3_rect.collidepoint(mouse_pos):
                button_colors[0] = [GRAY, GRAY, GREEN]
                print("Level: Hard")
            # Check algorithm options
            elif button4_rect.collidepoint(mouse_pos):
                button_colors[1] = [GREEN, GRAY, GRAY]
                print("Algorithm: A*")
            elif button5_rect.collidepoint(mouse_pos):
                button_colors[1] = [GRAY, GREEN, GRAY]
                print("Algorithm: Dijkstra")
            elif button6_rect.collidepoint(mouse_pos):
                button_colors[1] = [GRAY, GRAY, GREEN]
                print("Algorithm: BFS")

    # Fill the background
    screen.fill(WHITE)
    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
