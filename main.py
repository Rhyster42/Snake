import pygame
import sys
import random
from constants import *


def main():
    print("Hello Rhys!")
    
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake_Game")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    main()