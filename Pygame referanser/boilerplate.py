import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Konstanter
BREDDE = 720
HOEYDE= 1080
FPS = 30

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
RORD = (255, 0, 0)
GROENN = (0, 255, 0)
BLAA = (0, 0, 255)

# Initialiserer pygame lager vinduet
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOEYDE))
pygame.display.set_caption("<Spillnavn>")
clock = pygame.time.Clock()     # For å sette FPS


# Lager en variabel med alle sprites som gjør det enklere å oppdatere vinduet
alle_sprites = pygame.sprite.Group()
# alle_sprites.add(sprite)

# Spill løkka
fortsett = True
while fortsett:

    #1 Prosseserer pygame input
    clock.tick(FPS)     # Gjør at loopen tikker etter FPS - Stabilitet
    for event in pygame.event.get():        # Nødvendig for pygame
        # Ser etter om pygame skal avslutte
        if event.type == pygame.QUIT:
            running = False


    #2 Update
    alle_sprites.update()

    #3 Tegner bakgrunnen
    vindu.fill(SVART)

    alle_sprites.draw(vindu)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()