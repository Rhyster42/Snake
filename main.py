import pygame
import sys
import random
from constants import *
from snake import Snake
from fruit import Fruit
from gameborders import borders
from menus import show_game_over_screen


def main():
    print("Hello Rhys!")
    
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake_Game")
    clock = pygame.time.Clock()

    # Snake/Fruit initialized - start position
    snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2)
    fruit = Fruit()

    running = True
    game_over = False
    while running: # core game loop

        if not game_over:
            if snake.body[0] == (fruit.x, fruit.y): #eat fruit effects
                fruit.new_position()
                snake.grow_snake()

            for event in pygame.event.get(): # user controls
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_UP:
                        snake.change_direction(0, -1)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(0, 1)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(1, 0)

            snake.move()

            if snake.body[0][0] < 1 or snake.body[0][0] >= GRID_WIDTH - 1: # outside borders check
                game_over = True
            if snake.body[0][1] < 1 or snake.body[0][1] >= GRID_HEIGHT - 1:
                game_over = True

            for part in snake.body[1:]: # self collision detection
                if snake.body[0] == part:
                    game_over = True

            screen.fill(BLACK)
            fruit.draw(screen)
            snake.draw(screen)

            for border in borders:
                pygame.draw.rect(screen, BLUE, border)
        
            pygame.display.flip()
            # framerate
            clock.tick(10)

        else:

            show_game_over_screen(screen, snake.length)


    
    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()