import pygame
import random

# Initialiserer Pygame
pygame.init()

# Definerer vindusstørrelsen
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ditt Spill Navn")

# Definerer farger
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Definerer sonene
menneske_sone = pygame.Rect(0, 0, WINDOW_WIDTH//6, WINDOW_HEIGHT)
midtsone = pygame.Rect(WINDOW_WIDTH//6, 0, 2*WINDOW_WIDTH//3, WINDOW_HEIGHT)
saue_sone = pygame.Rect(5*WINDOW_WIDTH//6, 0, 1*WINDOW_WIDTH//6, WINDOW_HEIGHT)

# Definerer spilleren
player_size = 50
player_color = GREEN
player = pygame.Rect(50, WINDOW_HEIGHT//2 - player_size//2, player_size, player_size)

# Definerer sauene
sheep_size = 30
sheep_color = WHITE
sheep1 = pygame.Rect(2*WINDOW_WIDTH//3 + 50, 100, sheep_size, sheep_size)
sheep2 = pygame.Rect(2*WINDOW_WIDTH//3 + 150, 250, sheep_size, sheep_size)
sheep3 = pygame.Rect(2*WINDOW_WIDTH//3 + 250, 400, sheep_size, sheep_size)
sheep_list = [sheep1, sheep2, sheep3]

# Definerer hindringsobjekter
obstacle_size = 50
obstacle_color = BLUE
obstacle1 = pygame.Rect(WINDOW_WIDTH//3 + 100, 200, obstacle_size, obstacle_size)
obstacle2 = pygame.Rect(WINDOW_WIDTH//3 + 300, 350, obstacle_size, obstacle_size)
obstacle3 = pygame.Rect(WINDOW_WIDTH//3 + 500, 100, obstacle_size, obstacle_size)
obstacle_list = [obstacle1, obstacle2, obstacle3]

# Definerer spøkelsesobjekter
ghost_size = 40
ghost_color = (255, 0, 0)
ghost1 = pygame.Rect(WINDOW_WIDTH//3 + 100, 100, ghost_size, ghost_size)
ghost2 = pygame.Rect(WINDOW_WIDTH//3 + 300, 300, ghost_size, ghost_size)
ghost3 = pygame.Rect(WINDOW_WIDTH//3 + 500, 500, ghost_size, ghost_size)
ghost_list = [ghost1, ghost2, ghost3]

# Spillhovedløkke
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tegner bakgrunnen
    WINDOW.fill((0, 0, 0))

    # Tegner sonene
    pygame.draw.rect(WINDOW, (100, 100, 100), menneske_sone)
    pygame.draw.rect(WINDOW, (200, 200, 200), midtsone)
    pygame.draw.rect(WINDOW, (00, 00, 00), saue_sone)

    # Tegner spilleren
    pygame.draw.rect(WINDOW, player_color, player)

    # Tegner sauene
    for sheep in sheep_list:
        pygame.draw.rect(WINDOW, sheep_color, sheep)

    # Tegner hindringsobjekter
    for obstacle in obstacle_list:
        pygame.draw.rect(WINDOW, obstacle_color, obstacle)

    # Tegner spøkelsesobjekter
    for ghost in ghost_list:
        pygame.draw.rect(WINDOW, ghost_color, ghost)

    pygame.display.update()

pygame.quit()
