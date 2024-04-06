import pygame
import random

# Definerer farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Definerer globale variabler
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FREQUENCY = 5  # Endre for å endre spøkelsenes bevegelseshastighet
SPEED = 5  # Endre for å endre menneskets bevegelseshastighet

# Klassedefinisjoner
class SpillObjekt(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Menneske(SpillObjekt):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.speed_x = 0
        self.speed_y = 0

    def endre_retning(self, x, y):
        self.speed_x += x
        self.speed_y += y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Spøkelse(SpillObjekt):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.speed_x = random.choice([-1, 1]) * FREQUENCY
        self.speed_y = random.choice([-1, 1]) * FREQUENCY

    def update(self): 
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Hindring(SpillObjekt):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)

class Sau(SpillObjekt):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)

# Oppsett av spillet
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Manic Mansion")

# Oppretter spillebrettet
spillebrett = pygame.sprite.Group()

# Oppretter menneske
menneske = Menneske(RED, 50, 50)
menneske.rect.x = 50
menneske.rect.y = SCREEN_HEIGHT // 2
spillebrett.add(menneske)

# Oppretter spøkelser
for _ in range(3):
    spøkelse = Spøkelse(BLUE, 50, 50)
    spøkelse.rect.x = random.randrange(SCREEN_WIDTH)
    spøkelse.rect.y = random.randrange(SCREEN_HEIGHT)
    spillebrett.add(spøkelse)

# Oppretter hindringer
for _ in range(3):
    hindring = Hindring(BLACK, 50, 50)
    hindring.rect.x = random.randrange(SCREEN_WIDTH)
    hindring.rect.y = random.randrange(SCREEN_HEIGHT)
    spillebrett.add(hindring)

# Oppretter sauer
for _ in range(3):
    sau = Sau(GREEN, 50, 50)
    sau.rect.x = random.randrange(SCREEN_WIDTH // 2, SCREEN_WIDTH)
    sau.rect.y = random.randrange(SCREEN_HEIGHT)
    spillebrett.add(sau)

clock = pygame.time.Clock()
game_over = False

# Hovedløkke
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                menneske.endre_retning(-SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                menneske.endre_retning(SPEED, 0)
            elif event.key == pygame.K_UP:
                menneske.endre_retning(0, -SPEED)
            elif event.key == pygame.K_DOWN:
                menneske.endre_retning(0, SPEED)

    screen.fill(WHITE)

    spillebrett.update()

    # Sjekker kollisjoner
    kolliderer = pygame.sprite.spritecollide(menneske, spillebrett, False)
    for objekt in kolliderer:
        if isinstance(objekt, Spøkelse):
            game_over = True
        elif isinstance(objekt, Sau):
            spillebrett.remove(objekt)

    spillebrett.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
