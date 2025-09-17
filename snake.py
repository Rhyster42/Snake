import pygame
from constants import GRID_SIZE, GREEN

class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)] # list of coordinates for body parts
        self.direction = (1, 0)
        self.grow = False
        print("snake initialized")

    def move(self):
        head_x, head_y = self.body[0] # head position

        new_head = (head_x + self.direction[0], head_y + self.direction[1]) # calculate next position

        self.body.insert(0, new_head) # add new head to front

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx,dy)

    def grow_snake(self):
        self.grow = True

    def draw(self, screen):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE,
                               GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREEN, rect)


