import pygame
from konstanter import *
from karakterer import *
import random

# For å gi visuelt inntrykk av sonene. Har delt brettet i 6 deler, der midtsonen er 4/6 stor
menneske_sone = pygame.Rect(0, 0, BREDDE//6, HOEYDE)
midtsone = pygame.Rect(BREDDE//6, 0, 2*BREDDE//3, HOEYDE)
saue_sone = pygame.Rect(5*BREDDE//6, 0, 1*BREDDE//6, HOEYDE)

def vis_poeng(vindu, poeng):
    font = pygame.font.SysFont(None, 36)  # Velger font og størrelse
    tekst = font.render(f"Poeng: {poeng}", True, SVART)  # Lager tekstobjekt
    vindu.blit(tekst, (BREDDE - tekst.get_width() - 10, 10))  # Tegner tekstobjektet på skjermen


pygame.init()

def main():

    # Initialiserer pygame lager vinduet
    vindu = pygame.display.set_mode((BREDDE, HOEYDE))
    pygame.display.set_caption("Manic Mansion")
    clock = pygame.time.Clock()     # For å sette FPS

    # Oppretter spoekelseret
    spoekelser = pygame.sprite.Group()
    sauer = pygame.sprite.Group()
    hindringer = []
    holdt_sau = None

    # Karakterer
    menneske = Menneske((BREDDE/6)/2, HOEYDE/2, STARTSFART, BLAA, vindu)
    starts_antall = 3

    for _ in range(starts_antall):
        # Generer tilfeldige koordinater innenfor midtsonen
        x = random.randint(midtsone.left + 30, midtsone.right - 30)
        y = random.randint(midtsone.top + 30, midtsone.bottom - 30)
        # Oppretter spøkelse
        spokelse = Spoekelse(x, y, ROED, vindu, 5, 5, midtsone)
        spoekelser.add(spokelse)
        hindring = Hindring(x,y,SVART,vindu)
        hindringer.append(hindring)
        ny_sau = Sau(random.randint(saue_sone.left + 20, saue_sone.right - 20), random.randint(saue_sone.top + 20, saue_sone.bottom - 20), HVIT, vindu)
        sauer.add(ny_sau)

    

    # Spill løkka
    fortsett = True
    while fortsett:

        # Prossesere pygame input
        for event in pygame.event.get():        # Nødvendig for pygame
            # Ser etter om pygame skal avslutte
            if event.type == pygame.QUIT:
                fortsett = False
    
        # Bevegelsesrelatert funksjonalitet
        trykkede_taster = pygame.key.get_pressed()
        menneske.flytt(trykkede_taster,hindringer)
        for spokelse in spoekelser:
            spokelse.flytt()
        
        # Kollisjonsrelatert funksjonalitet

        # Kollisjon med spøkelse:
        kolliderende_spoekelser = pygame.sprite.spritecollide(menneske, spoekelser, False)
        if kolliderende_spoekelser:
            # Mennesket kolliderer med et spøkelse
            print("Mennesket har kollidert med et spøkelse!")
            fortsett = False  # Avslutt spillet

        # Kollisjon med sau:
        kolliderende_sauer = pygame.sprite.spritecollide(menneske, sauer, True)
        for sau in kolliderende_sauer:
            if holdt_sau is None:
                holdt_sau = sau
                menneske.fart -= FARTSFAKTOR  # Reduserer spillerens fart når han holder på en sau
                menneske.farge = GROENN
            else:
                # Spillet avsluttes hvis spilleren allerede holder på en sau og treffer en annen sau
                fortsett = False

        # Sjekker om mennesket har kommet tilbake til menneskesonen med en sau
        if menneske.rect.colliderect(menneske_sone):
            if holdt_sau is not None:
                # Øker poeng og fjerner sau
                menneske.poeng += 1
                sauer.remove(holdt_sau)
                holdt_sau = None
                menneske.fart += FARTSFAKTOR  # Setter spillerens fart tilbake til normalt
                menneske.farge = BLAA

                # Legger til ny sau
                ny_sau = Sau(random.randint(saue_sone.left + 20, saue_sone.right - 20),
                             random.randint(saue_sone.top + 20, saue_sone.bottom - 20),
                             HVIT, vindu)
                sauer.add(ny_sau)

                # Legger til nytt spøkelse og hindring
                x = random.randint(midtsone.left + 20, midtsone.right - 20)
                y = random.randint(midtsone.top + 20, midtsone.bottom - 20)
                nytt_spokelse = Spoekelse(x, y ,ROED, vindu, 5, 5, midtsone)
                spoekelser.add(nytt_spokelse)
                hindring = Hindring(x,y,SVART,vindu)
                hindringer.append(hindring)

        
        # Tegner karakterer og bakgrunnen
        vindu.fill(SVART)
        
        pygame.draw.rect(vindu, (100, 100, 100), menneske_sone)
        pygame.draw.rect(vindu, (200, 200, 200), midtsone)
        pygame.draw.rect(vindu, (100, 100, 100), saue_sone)

        menneske.tegn()
        spoekelser.draw(vindu)
        sauer.draw(vindu)
        for hindring in hindringer:
            hindring.tegn()

        vis_poeng(vindu,menneske.poeng)
        clock.tick(FPS)     # Gjør at loopen tikker etter FPS - Stabilitet
        pygame.display.flip()  

if __name__ == '__main__':
    main()
    pygame.quit()