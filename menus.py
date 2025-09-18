import pygame
from constants import BLACK, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT

def show_game_over_screen(screen, score):
    global game_over
    global running

    screen.fill(BLACK)

    font_large = pygame.font.Font(None, 80)
    game_over_text = font_large.render("Game Over", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 50))
    screen.blit(game_over_text, game_over_rect)

    font_small = pygame.font.Font(None, 40)
    score_text = font_small.render(f'Final Score: {score}', True, WHITE)
    score_rect = score_text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 20))
    screen.blit(score_text, score_rect)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting_for_input = False
                    game_over = False # Reset the game_over state
