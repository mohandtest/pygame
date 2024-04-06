from math import sqrt
from pygame import draw, sprite
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)


class SuperKarakter(sprite.Sprite):
    """Klasse for karakter"""
    def __init__(self, x, y, radius, farge, vindusobjekt):
        """Konstruktør"""
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vindusobjekt = vindusobjekt


    def tegn(self):
        """Metode for å tegne ballen"""
        draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

    def finnAvstand(self, annetObjekt):
        """Metode for å finne avstanden til en annen ball"""
        xAvstand2 = (self.x - annetObjekt.x)**2  # x-avstand i andre
        yAvstand2 = (self.y - annetObjekt.y)**2  # y-avstand i andre
        sentrumsavstand = sqrt(xAvstand2 + yAvstand2)
        radiuser = self.radius + annetObjekt.radius
        avstand = sentrumsavstand - radiuser
        return avstand  
    

class Menneske(SuperKarakter):
    def __init__(self, x, y, fart, radius, farge, vindusobjekt):
        super().__init__(x, y, radius, farge, vindusobjekt)
        self.fart = fart
        
    def tegn(self):
        """Metode for å tegne spilleren"""
        draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

    def flytt(self, taster):
      """Metode for å flytte ballen"""
      if taster[K_UP]:
        self.y -= self.fart
      if taster[K_DOWN]:
        self.y += self.fart
      if taster[K_LEFT]:
        self.x -= self.fart
      if taster[K_RIGHT]:
        self.x += self.fart

        


class Spoekelse(SuperKarakter):
  """Klasse for å representere et hinder"""
  def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.xFart = xFart
    self.yFart = yFart

  def flytt(self):
    """Metode for å flytte spøkelset"""
    # Sjekker om hinderet er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.xFart = -self.xFart
    
    # Sjekker om hinderet er utenfor øvre/nedre kant
    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.yFart = -self.yFart

    # Flytter hinderet
    self.x += self.xFart
    self.y += self.yFart
