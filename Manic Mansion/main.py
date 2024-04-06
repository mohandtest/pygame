import pygame
from konstanter import *
from karakterer import Menneske

# For å gi visuelt inntrykk av sonene. Har delt brettet i 6 deler, der midtsonen er 4/6 stor
menneske_sone = pygame.Rect(0, 0, BREDDE//6, HOEYDE)
midtsone = pygame.Rect(BREDDE//6, 0, 2*BREDDE//3, HOEYDE)
saue_sone = pygame.Rect(5*BREDDE//6, 0, 1*BREDDE//6, HOEYDE)

# Initialiserer pygame lager vinduet
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOEYDE))
pygame.display.set_caption("Manic Mansion")
clock = pygame.time.Clock()     # For å sette FPS

# Oppretter spillebrettet
spillebrett = pygame.sprite.Group()

menneske = Menneske(BREDDE/6, HOEYDE/2, 4, 15,BLAA,vindu)

# Spill løkka
fortsett = True
while fortsett:

    #1 Prosseserer pygame input
    for event in pygame.event.get():        # Nødvendig for pygame
        # Ser etter om pygame skal avslutte
        if event.type == pygame.QUIT:
            fortsett = False
 

    trykkede_taster = pygame.key.get_pressed()
    menneske.flytt(trykkede_taster)

    #3 Tegner karakterer og bakgrunnen
    vindu.fill(SVART)
    pygame.draw.rect(vindu, (100, 100, 100), menneske_sone)
    pygame.draw.rect(vindu, (200, 200, 200), midtsone)
    pygame.draw.rect(vindu, (100, 100, 100), saue_sone)
    menneske.tegn()


    clock.tick(FPS)     # Gjør at loopen tikker etter FPS - Stabilitet
    pygame.display.flip()  
pygame.quit()