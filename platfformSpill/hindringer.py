
from pygame import draw, sprite, Rect, Surface

class Hindring(sprite.Sprite):
    def __init__(self, x, y, farge, vindusobjekt, bredde=30, hoeyde=30):
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
      """Tegner karaketeren som et rektankgel med de gitte parameterene"""
      draw.rect(self.vindusobjekt, self.farge, (self.rect.x, self.rect.y, self.bredde, self.hoeyde))
