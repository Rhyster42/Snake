import pygame
from constants import GRID_SIZE, GRID_HEIGHT, GRID_WIDTH, RED
import random

class Fruit:
    def __init__(self):
        self.x = random.randint(0, GRID_WIDTH)
        self.y = random.randint(0, GRID_HEIGHT) # Initialize with random position

    def draw(self, screen):
        rect = pygame.Rect(self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, rect)

    def new_position(self):
        self.x = random.randint(0, GRID_WIDTH)
        self.y = random.randint(0, GRID_HEIGHT)