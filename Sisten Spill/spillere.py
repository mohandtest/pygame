from farger import *

#Klasse for spilleren
class Spiller:
    def __init__(self, color, start_row, start_col):
        self.color = color
        self.row = start_row
        self.col = start_col
        self.points = 0

    #Bevegelse:
    def move(self, direction):
        if direction == "UP" and self.row > 0 and spill.spillbrett[self.row - 1][self.col] != "W":
            self.row -= 1
        elif direction == "DOWN" and self.row < len(spill.spillbrett) - 1 and spill.spillbrett[self.row + 1][self.col] != "W":
            self.row += 1
        elif direction == "LEFT" and self.col > 0 and spill.spillbrett[self.row][self.col - 1] != "W":
            self.col -= 1
        elif direction == "RIGHT" and self.col < len(spill.spillbrett[0]) - 1 and spill.spillbrett[self.row][
            self.col + 1] != "W":
            self.col += 1

#Tvinger inn arv (selv om det er litt unødvendig her)
class RoedSpiller(Spiller):
    def __init__(self, start_row, start_col):
        super().__init__(ROED, start_row, start_col)

class BlaaSpiller(Spiller):
    def __init__(self, start_row, start_col):
        super().__init__(BLAA, start_row, start_col)
