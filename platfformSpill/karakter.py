from pygame.locals import (K_UP, K_LEFT, K_RIGHT)
from pygame import draw, sprite, Vector2, Rect, Surface

class Spiller(sprite.Sprite):
    """Klasse for karakter"""
    def __init__(self, x, y, farge, vindusobjekt, fart, poeng=0, bredde=30, hoeyde=30):
        """Konstruktør"""
        super().__init__()
        self.x = x
        self.y = y
        self.farge = farge
        self.vindusobjekt = vindusobjekt
        self.bredde = bredde
        self.hoeyde = hoeyde
        self.isJump = False
        self.jumpCount = 10
        self.hoppeFaktor = 1
        self.tyngde = 2  # Tyngdekraft

        self.image = Surface((self.bredde, self.hoeyde))
        self.image.fill(farge)
        self.rect = self.image.get_rect()
        self.rect = Rect(x, y, self.bredde, self.hoeyde)
        self.fart = fart
        self.forrige_posisjon = self.rect.copy()  # Lagre forrige gyldige posisjon
        self.forrige_hoyde = self.y  # Lagre forrige høyde for å sjekke om spilleren har landet

        # Definer bakken som et rektangel som dekker hele spillvinduet
        self.bakke = Rect(0, vindusobjekt.get_height() - 50, vindusobjekt.get_width(), 50)

    def tegn(self):
        """Tegner karakteren som et rektangel med de gitte parameterene"""
        draw.rect(self.vindusobjekt, self.farge, (self.rect.x, self.rect.y, self.bredde, self.hoeyde))

    def sjekk_kollisjon(self, hindring):
        """Sjekker om karakteren kolliderer med hindringen"""
        return self.rect.colliderect(hindring.rect)

    def handle_kollisjon(self, hindringer):
        """Håndterer kollisjon med hindringer"""
        for hindring in hindringer:
            if self.sjekk_kollisjon(hindring):
                self.rect = self.forrige_posisjon  # Flytt tilbake til forrige gyldige posisjon
                break

    def flytt(self, taster, hindringer):
        """Metode for å flytte karakteren"""
        retning = Vector2(0, 0)

        if taster[K_UP]:
            if not self.isJump:  # Start hopp kun hvis spilleren ikke allerede hopper
                self.isJump = True
                self.forrige_hoyde = self.y  # Lagre forrige høyde før hoppet

        if taster[K_LEFT]:
            retning.x -= self.fart
        if taster[K_RIGHT]:
            retning.x += self.fart

        if self.isJump:
            if self.jumpCount >= -10:
                retning.y -= self.jumpCount * 1
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False


        # Lagre forrige gyldige posisjon
        self.forrige_posisjon = self.rect.copy()

        # Beregn ny posisjon
        ny_rektangel = self.rect.move(retning)

        # Begrens bevegelsen til å holde karakteren innenfor vinduet
        ny_rektangel.x = max(0, min(ny_rektangel.x, self.vindusobjekt.get_width() - self.bredde))
        ny_rektangel.y = max(0, min(ny_rektangel.y, self.vindusobjekt.get_height() - self.hoeyde))

        # Oppdater posisjonen
        self.rect = ny_rektangel

        # Håndter kollisjon
        self.handle_kollisjon(hindringer)

    def sjekk_tyngdekraft(self, bakke_hoyde, hindringer):
        """Sjekk og håndter tyngdekraften for spilleren"""
        if not self.isJump and self.rect.y < bakke_hoyde:
            for hindring in hindringer:
                if self.rect.colliderect(hindring.rect):
                    return
            self.rect.y += self.tyngde