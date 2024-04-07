from math import sqrt
from pygame import draw, sprite, Vector2, Rect, Surface
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)


class SuperKarakter(sprite.Sprite):
    """Klasse for karakter"""
    def __init__(self, x, y, farge, vindusobjekt, bredde = 20, hoeyde = 20):
        """Konstruktør"""
        super().__init__()
        self.x = x
        self.y = y
        self.farge = farge
        self.vindusobjekt = vindusobjekt
        self.bredde = bredde
        self.hoeyde = hoeyde
        self.image = Surface((self.bredde, self.hoeyde))
        self.image.fill(farge)
        self.rect = self.image.get_rect()
        self.rect = Rect(x , y, self.bredde,self.hoeyde)


    def tegn(self):
      draw.rect(self.vindusobjekt, self.farge, (self.rect.x, self.rect.y, self.bredde, self.hoeyde)) 

    def sjekk_kollisjon(self, karakter):
        """Sjekker om karakteren kolliderer med hindringen"""
        return self.rect.colliderect(karakter.rect)

class Menneske(SuperKarakter):
    def __init__(self, x, y, fart, farge, vindusobjekt, poeng = 0):
        super().__init__(x, y, farge, vindusobjekt, bredde = 20 , hoeyde= 20)
        self.fart = fart
        self.poeng = poeng
      
    def flytt(self, taster, hindringer):
        """Metode for å flytte mennesket"""
        retning = Vector2(0, 0)
        if taster[K_UP]:
            retning.y -= 1
        if taster[K_DOWN]:
            retning.y += 1
        if taster[K_LEFT]:
            retning.x -= 1
        if taster[K_RIGHT]:
            retning.x += 1

        # Hvis spilleren beveger seg diagonalt, normaliser retningen og deler med sqrt(2)
        if retning.length() > 0:
            retning.normalize_ip()
            retning *= self.fart
        retning = round(retning)
        # Beregn ny posisjon
        ny_x = self.rect.x + retning.x
        ny_y = self.rect.y + retning.y

        # Opprett en rektangel for å representere den potensielle nye posisjonen
        ny_rektangel = Rect(ny_x, ny_y, self.bredde, self.hoeyde)

        # Sjekk for kollisjon med hindringer
        kollisjon = False
        for hindring in hindringer:
            if hindring.sjekk_kollisjon(self):
                kollisjon = True
                break

        # Hvis det er en kollisjon, juster den potensielle nye posisjonen
        if kollisjon:
            # Finn forskjellen mellom spillerens midtpunkt og hindringens midtpunkt
            diff_x = hindring.rect.centerx - self.rect.centerx
            diff_y = hindring.rect.centery - self.rect.centery
            # Hvis hindringen er nærmere i x-retning
            if abs(diff_x) > abs(diff_y):
                # Juster den potensielle nye posisjonen i x-retning
                ny_rektangel.x -= retning.x
            else:
                # Juster den potensielle nye posisjonen i y-retning
                ny_rektangel.y -= retning.y

        # Begrens bevegelsen til å holde spilleren innenfor vinduet
        ny_rektangel.x = max(0, min(ny_rektangel.x, self.vindusobjekt.get_width() - self.bredde))
        ny_rektangel.y = max(0, min(ny_rektangel.y, self.vindusobjekt.get_height() - self.hoeyde))

        # Oppdater posisjonen
        self.rect = ny_rektangel



class Spoekelse(SuperKarakter):
    """Klasse for å representere et hinder"""

    def __init__(self, x, y, farge, vindusobjekt, xFart, yFart, sone):
        super().__init__(x, y, farge, vindusobjekt, bredde=20, hoeyde=20)
        self.xFart = xFart
        self.yFart = yFart
        self.sone = sone
        

    def flytt(self):
        """Metode for å flytte spøkelset"""
        # Sjekk om hinderet er i midtsonen
        if self.sone.colliderect(self.rect):
            # Sjekker om hinderet er utenfor venstre/høyre kant
            if ((self.x - self.bredde) <= self.sone.left) or ((self.x + self.bredde) >= self.sone.right):
                self.xFart = -self.xFart

            # Sjekker om hinderet er utenfor øvre/nedre kant
            if ((self.y - self.hoeyde) <= self.sone.top) or ((self.y + self.hoeyde) >= self.sone.bottom):
                self.yFart = -self.yFart

        # Flytter hinderet
        self.x += self.xFart
        self.y += self.yFart
        self.rect.centerx = self.x
        self.rect.centery = self.y

class Hindring(SuperKarakter):
    def __init__(self, x, y, farge, vindusobjekt, bredde=20, hoeyde=20):
        super().__init__(x, y, farge, vindusobjekt, bredde, hoeyde)

    
class Sau(SuperKarakter):
    def __init__(self, x, y, farge, vindusobjekt, bredde=20, hoeyde=20):
        super().__init__(x, y, farge, vindusobjekt, bredde, hoeyde)
