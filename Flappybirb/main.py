import pygame
from spillobjekter import *



# Konstanter
BREDDE = 500
HOEYDE = 600
FPS = 35
HVIT = (255, 255, 255)

# Initialiserer pygame og lager vinduet
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOEYDE))
pygame.display.set_caption("FlOpPyBIrb")
clock = pygame.time.Clock()  # For å sette FPS

birb = Bird(vindu)
pipe = Pipe(BREDDE, HOEYDE)
piper = []
piper.append(pipe)

font = pygame.font.Font(None, 36)  # Font for poengvisning
high_score = 0

# Spill-løkke
fortsett = True
while fortsett:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False

    taster = pygame.key.get_pressed()
    birb.flap(taster)
    birb.update(pipe)

    for pipe in piper:
        pipe.update()

        # Sjekk kollisjon med hver pipe
        if birb.rect.colliderect(pipe.rect_top) or birb.rect.colliderect(pipe.rect_bottom):
            birb.reset()
            pipe.reset()
            high_score = max(high_score, birb.score)

        # Sjekk om fuglen har passert gjennom et rør
        if pipe.x < birb.x and not pipe.passed:
            birb.score += 1
            pipe.passed = True


    vindu.fill(HVIT)
    birb.draw()
    for pipe in piper:
        pipe.draw(vindu)

    if birb.score > high_score:
        high_score = birb.score
    # Vis poeng
    score_text = font.render(f"Poeng: {birb.score} | Highscore: {high_score}", True, (0, 0, 0))
    vindu.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
