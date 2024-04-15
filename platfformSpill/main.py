import pygame
from konstanter import *
from karakter import Spiller
from hindringer import *
# Initialiserer pygame lager vinduet
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOEYDE))
pygame.display.set_caption("Plattform")
clock = pygame.time.Clock()     # For å sette FPS

spiller = Spiller(0,HOEYDE,SVART,vindu,5)

hindringer = []


# Spill løkka
fortsett = True
while fortsett:
    # Prossesere pygame input
    for event in pygame.event.get():        # Nødvendig for pygame
        # Ser etter om pygame skal avslutte
        if event.type == pygame.QUIT:
            fortsett = False    

    trykkede_taster = pygame.key.get_pressed()
    spiller.flytt(trykkede_taster,hindringer)
    spiller.sjekk_tyngdekraft(HOEYDE+30,hindringer)

    

    #3 Tegner bakgrunnen
    vindu.fill(HVIT)
    spiller.tegn()

    


    clock.tick(FPS)
    pygame.display.flip()       

pygame.quit()