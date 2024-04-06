import pygame as pg
from pygame.locals import *
import random

from spillere import RoedSpiller, BlaaSpiller
from farger import *

# En stor spillklasse med nesten alt av spilllogikken (for å tvinge meg selv til å jobbe objektorientert)
class Spill:
    def __init__(self, window_width, window_height, cell_size, cell_margin):
        
        # Initerer pygame og setter opp noen egenskaper for vinduet/brettet
        pg.init()
        self.clock = pg.time.Clock()
        self.window_width = window_width
        self.window_height = window_height
        self.window = pg.display.set_mode((self.window_width, self.window_height))
        pg.display.set_caption("Spillbrett")
        self.font = pg.font.Font(None, 36)
        self.cell_size = cell_size
        self.cell_margin = cell_margin
        self.running = True

        #Her er et 22x22 spillerbrett (21x21 hvis man ignorerer ytterkanten) - Kunne nok blitt gjort på en annen måte, men dette fungerer for meg.
        self.spillbrett = [
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", "W", "W", "W", "W", "W", "W", "W"," ", " ", " ", "W", "W", "W", "W", "W", "W", "W", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " ", "W","W", "W", "W", "W", " ", " ", "W", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " ", " "," ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " ", " "," ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " "," ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", "W", " ", " ", "W","W", "W", "W", "W", " ", " ", "W", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", "W", "W", "W", "W", "W", "W", "W"," ", " ", " ", "W", "W", "W", "W", "W", "W", "W", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W","W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
        ]
        
        #Setter spillerene og nektar i posisjonene deres
        self.spiller1 = RoedSpiller(1, 1) # Toppen til venstre
        self.spiller2 = BlaaSpiller(len(self.spillbrett) - 2, len(self.spillbrett[0]) - 2) # Nedre ventre hjørne
        self.nektar = (len(self.spillbrett) // 2, len(self.spillbrett) // 2) # Midten

    #Eventhandler for brukerinputt
def handle_events(self):
    for event in pg.event.get():
        if event.type == QUIT:
            self.running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                self.spiller1.move("UP", self)
            elif event.key == K_DOWN:
                self.spiller1.move("DOWN", self)
            elif event.key == K_LEFT:
                self.spiller1.move("LEFT", self)
            elif event.key == K_RIGHT:
                self.spiller1.move("RIGHT", self)
            elif event.key == K_w:
                self.spiller2.move("UP", self)
            elif event.key == K_s:
                self.spiller2.move("DOWN", self)
            elif event.key == K_a:
                self.spiller2.move("LEFT", self)
            elif event.key == K_d:
                self.spiller2.move("RIGHT", self)

    #Respawner nektaren i en random posisjon som ikke er en vegg
    def respawn_nektar(self):
        while True:
            row = random.randint(0, len(self.spillbrett) - 1)
            col = random.randint(0, len(self.spillbrett[0]) - 1)
            if self.spillbrett[row][col] != "W":
                return row, col

    # Hendelseshåndtering (kollisjoner)
    def oppdater(self):
        if (self.spiller1.row, self.spiller1.col) == self.nektar:
            self.spiller1.points += 1
            self.nektar = self.respawn_nektar()

        if (self.spiller2.row, self.spiller2.col) == self.nektar:
            self.spiller2.points += 1
            self.nektar = self.respawn_nektar()

        if (
            self.spillbrett[self.spiller1.row][self.spiller1.col] == "W"
            or (self.spiller1.row, self.spiller1.col) == (self.spiller2.row, self.spiller2.col)
        ):
            self.running = False

            if self.spiller1.points == self.spiller2.points:
                print("Det er uavgjort!")
            else:
                winner = "Rød" if self.spiller1.points > self.spiller2.points else "Blå"
                print(f"{winner} spiller vinner!")

    # Tegner brettet og spillere
    def draw(self):
        self.window.fill(HVIT)

        for row in range(len(self.spillbrett)):
            for column in range(len(self.spillbrett[row])):
                color = HVIT
                if self.spillbrett[row][column] == "W":
                    color = SVART
                elif self.spillbrett[row][column] == "N":
                    color = GUL
                elif (row, column) == (self.spiller1.row, self.spiller1.col):
                    color = self.spiller1.color
                elif (row, column) == (self.spiller2.row, self.spiller2.col):
                    color = self.spiller2.color
                elif (row, column) == self.nektar:
                    color = GUL

                pg.draw.rect(
                    self.window,
                    color,
                    (
                        (self.cell_margin + self.cell_size) * column + self.cell_margin,
                        (self.cell_margin + self.cell_size) * row + self.cell_margin,
                        self.cell_size,
                        self.cell_size,
                    ),
                )

        # Poengteksten
        roed_text = self.font.render(f"Rød: {self.spiller1.points}", True, ROED)
        blaa_text = self.font.render(f"Blå: {self.spiller2.points}", True, BLAA)
        self.window.blit(roed_text, (self.window_width - roed_text.get_width(), 0))
        self.window.blit(blaa_text, (self.window_width - blaa_text.get_width(), roed_text.get_height()))

        #Oppdaterer skjermen og capper den til 60fps
        pg.display.flip()
        self.clock.tick(60)

    #Her er løkka, litt fint å se at kun ha tre metoder trengs for at spillet skal kjøre
    def run(self):
        while self.running:
            self.handle_events()
            self.oppdater()
            self.draw()

        pg.quit()

