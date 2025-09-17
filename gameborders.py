import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, WALL_THICKNESS

border_top = pygame.Rect(0, 0, WINDOW_WIDTH, WALL_THICKNESS)
border_bottom = pygame.Rect(0, WINDOW_HEIGHT - WALL_THICKNESS, WINDOW_WIDTH, WALL_THICKNESS)
border_left = pygame.Rect(0, 0, WALL_THICKNESS, WINDOW_HEIGHT)
border_right = pygame.Rect(WINDOW_WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, WINDOW_HEIGHT)

borders = [border_top, border_bottom, border_left, border_right]