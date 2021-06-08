import pygame
import sys


def check_win(massive, sign):
    if all(elem == sign for row in massive for elem in row):
        # The same sign in row
        return sign
    for col in range(3):
        if sign == massive[0][col] == massive[1][col] == massive[2][col]:
            # The same sign in column
            return sign
    if sign == massive[0][0] == massive[1][1] == massive[2][2]:
        # The same sign in cross
        return sign
    if sign == massive[0][2] == massive[1][1] == massive[2][0]:
        # The same sign in cross
        return sign
    if not any(element == 0 for row in massive for element in row):
        # All squares are filled with either "x" or "o" -> draw
        return "Draw"
    return False


pygame.init()

# Initializing window properties
size_block = 100
margin = 15
width = height = size_block * 3 + margin * 4
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-tac-toe")

# Initializing color
black = (0,0,0)
red = (255,0,0)
green = (0, 255, 0)
white = (255,255,255)

# Saving the state of each rectangle
massive = [[0]*3 for _ in range(3)]

# Keeping the order of players
query = 0  # 1, 2, 3, ...

# Keeping the state of game
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f"x={x_mouse}, y={y_mouse}")
            column = x_mouse // (margin + size_block)
            row = y_mouse // (margin + size_block)
            if not massive[row][column]:
                if query % 2 == 0:
                    massive[row][column] = "x"
                else:
                    massive[row][column] = "o"
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            massive = [[0]*3 for _ in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            y = row * (size_block + margin) + margin
            for column in range(3):
                x = column * (size_block + margin) + margin
                if massive[row][column] == "x":
                    color = red
                elif massive[row][column] == "o":
                    color = green
                else:
                    color = white
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x+5,y+5), (x+ size_block-5, y+size_block-5), 3)
                    pygame.draw.line(screen, white, (x+5,y+size_block-5), (x+ size_block-5, y+5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x+size_block/2, y+size_block/2), size_block/2 - 3, 3)
    # Checking the win
    if (query-1) % 2 == 0:
        # Checking the win of x
        game_over = check_win(massive, "x")
    else:
        # Checking the win of o
        game_over = check_win(massive, "o")
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont("stxingkai", 80)
        rendered_text = font.render(game_over, True, white)
        text_rect = rendered_text.get_rect()
        text_x = (screen.get_width() - text_rect.width) / 2
        text_y = (screen.get_height() - text_rect.height) / 2
        screen.blit(rendered_text, [text_x, text_y])
    pygame.display.update()
