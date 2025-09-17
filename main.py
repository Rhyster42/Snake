import pygame
import sys
import random
from constants import *
from snake import Snake
from fruit import Fruit


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
    while running:

        if snake.body[0] == (fruit.x, fruit.y):
            fruit.new_position()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)

        snake.move()

        screen.fill(BLACK)
        fruit.draw(screen)
        snake.draw(screen)
        pygame.display.flip()
        # framerate
        clock.tick(10)

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()