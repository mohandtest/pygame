from pygame import Rect, draw, sprite
from pygame.locals import K_SPACE, K_UP, K_w
from random import randint

class Bird(sprite.Sprite):
    def __init__(self, vindu):
        super().__init__()
        self.width = 40
        self.height = 40
        self.x = 100
        self.y = 300
        self.velocity = 0
        self.gravity = 1
        self.lift = -10
        self.score = 0

        self.vindu = vindu
        self.farge = (0, 0, 0)
        self.rect = Rect(self.x, self.y, self.width, self.height)  # Definerer rektangulær hitboks

    def flap(self, trykkede_taster):
        if (trykkede_taster[K_SPACE] or trykkede_taster[K_UP] or trykkede_taster[K_w]):
            self.velocity = self.lift

    def update(self,pipe):
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect.y = self.y  # Oppdater y-posisjonen til hitboksen

        # Sjekk om fuglen går utenfor vinduet
        if self.rect.bottom < 0 or self.rect.top > self.vindu.get_height():
            self.reset()
            pipe.reset()

    def draw(self):
        draw.rect(self.vindu, self.farge, self.rect)  # Tegn rektangel

    def reset(self):
        self.y = 300
        self.rect.y = 300
        self.velocity = 0
        self.score = 0


class Pipe:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pipe_width = 60
        self.min_pipe_height = 100
        self.max_pipe_height = self.screen_height - 160
        self.gap = 160
        self.speed = 12
        self.reset()

    def reset(self):
        self.x = self.screen_width
        self.top_pipe_height = randint(self.min_pipe_height, self.max_pipe_height)
        self.bottom_pipe_height = self.screen_height - self.gap - self.top_pipe_height
        self.passed = False

        # Oppdater rektangler for rørene
        self.rect_top = Rect(self.x, 0, self.pipe_width, self.top_pipe_height)
        self.rect_bottom = Rect(self.x, self.screen_height - self.bottom_pipe_height, self.pipe_width, self.bottom_pipe_height)

    def update(self):
        self.x -= self.speed

        # Oppdater posisjonen til rektangler for rørene
        self.rect_top.x = self.x
        self.rect_bottom.x = self.x

        if self.x < -self.pipe_width:
            self.reset()

    def draw(self, screen):
        draw.rect(screen, (0, 255, 0), self.rect_top)
        draw.rect(screen, (0, 255, 0), self.rect_bottom)
