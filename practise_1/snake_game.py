import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Define display dimensions
WIDTH, HEIGHT = 600, 400
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Define clock
CLOCK = pygame.time.Clock()
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Define font
FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = SCORE_FONT.render("Your Score: " + str(score), True, BLACK)
    DISPLAY.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(DISPLAY, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = FONT_STYLE.render(msg, True, color)
    DISPLAY.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            DISPLAY.fill(BLUE)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        DISPLAY.fill(BLUE)
        pygame.draw.rect(DISPLAY, GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

gameLoop()