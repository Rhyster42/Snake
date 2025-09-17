import pygame
from constants import GRID_SIZE, GRID_HEIGHT, GRID_WIDTH, RED
import random

class Fruit:
    def __init__(self):
        self.x = random.randint(2, GRID_WIDTH - 2)
        self.y = random.randint(2, GRID_HEIGHT - 2) # Initialize with random position

    def draw(self, screen):
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, rect)

    def new_position(self):
        self.x = random.randint(2, GRID_WIDTH - 2)
        self.y = random.randint(2, GRID_HEIGHT - 2)