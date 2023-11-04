import sys
import time
import pygame
from typing import List
from consts import Data, DataSorter, Size

def animate(num_seconds : float) -> float:
    """Giver (yields) antal sekunder siden generator-funktionen blev kaldt, i et tidsrum angivet ved 'num_seconds'"""
    initial_time = time.time()
    while time.time() - initial_time < num_seconds:
        yield (time.time() - initial_time) / num_seconds

class Visualizer:
    def __init__(self, title : str = "Sketch", size : Size = (600, 600)) -> None:
        """Initialiserer 'Visualizer'-objektet samt biblioteket pygame \\
           Laver et pygame-vindue med en titel angivet af 'title' og en vindue-størrelse angivet af 'size'"""

        self.width, self.height = size

        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.fonts = {
            "title": pygame.font.SysFont("arialblack", 30),
            "text": pygame.font.SysFont("calibri", 20),
            "large-text": pygame.font.SysFont("calibri", 40)
        }

    def quit(self) -> None:
        """Afslutter pygame og derefter programmet"""
        pygame.quit()
        sys.exit(0)
    
    def update(self) -> None:
        """Opdaterer skærmen og søger efter 'QUIT'-events (dvs. hvis brugeren lukker vinduet)"""
        if pygame.event.peek(eventtype = pygame.QUIT): self.quit()
        self.clock.tick()
        pygame.display.flip()

    def sleep(self, num_seconds : float) -> None:
        """Stoper visualiseringen 'num_seconds' sekunder"""
        if num_seconds <= 0: 
            self.update()
            return
        
        start_time = time.time()
        while time.time() - start_time < num_seconds: self.update()

    def halt(self):
        """Stopper visualiseringen indtil brugeren lukker vinduet"""
        while True: self.update()

    def await_press(self, key : str = ""):
        """Stopper visualiseringen indtil brugeren klikker på en bestem knap angivet ved 'key' \\
           Hvis 'key' er en tom string, vil programmet acceptere alle knapper"""

        while True:
            for event in pygame.event.get(eventtype = pygame.KEYDOWN):
                if key == "": return
                if pygame.key.name(event.key).lower() == key.lower(): return
            self.update()

    def bar_animation(self, algorithm : DataSorter, data : Data, time_interval : float = 0.01, title : str = "", expected_big_o : str = "") -> None:
        """Animation hvor en bestemt algoritme (angivet ved 'algorithm') sorterer et datasæt (angivet ved 'data') \\
           Efter hvert sorterings-step ventes der i 'time_interval' antal sekunder (hvis 0 stoppes der ikke) \\
           I animationen repræsenteres hvert datapunkt ved en lodret kolonne, hvis højde er lig datapunktets værdi \\
           Der vises en tekstboks, som består af en titel (angivet ved 'title') samt algoritmens tidskompleksitet (angivet ved 'expected_big_o') """

        text_surfs = [
            self.fonts["title"].render(title, False, (180, 180, 180)),
            self.fonts["text"].render(f"Antal datapunkter (n): {len(data)}", False, (180, 180, 180)),
            self.fonts["text"].render(f"Tidskompleksitet: {expected_big_o}", False, (180, 180, 180))
        ]

        for data_copy, indices in algorithm(data):
            self.screen.fill((35, 35, 35))

            for i, val in enumerate(data_copy):
                w, h = self.width / len(data_copy), self.height * val
                color = (170, 40, 40) if i in indices else (90, 90, 90)
                pygame.draw.rect(self.screen, color, (w * i, self.height - h, w, h))
            
            pygame.draw.rect(self.screen, (45, 45, 45), (10, 10, 280, 90))

            for i, text_surf in enumerate(text_surfs):
                self.screen.blit(text_surf, (20, 20 + i * 25))

            self.sleep(time_interval)
        
    def box_animation(self, algorithm : DataSorter, data : Data, title : str = "") -> None:
        """Animation hvor en bestemt algoritme (angivet ved 'algorithm') sorterer et datasæt (angivet ved 'data') \\
           I animationen repræsenteres hvert datapunkt ved en firkant, som kan bytte plads med andre firkanter efter hvert sorterings-step \\
           Der vises en tekstboks, som består af en titel (angivet ved 'title') \\
           Animationen virker kun hvis algoritmen virker ved at bytte rundt på to elementer, uden at holde nogen værdier i et midlertidigt lager (f.eks. virker bubble-sort, selection-sort og shell-sort)"""

        box_size = 60
        data_len = len(data)
        animation_time = 0.5
        title_surf = self.fonts["title"].render(title, False, (180, 180, 180))

        def draw_box(index : int, val : int | float, x_offset : float = 0, y_offset : float = 0):
            """Funktion der kan tegne en enkel firkant korrekt på skærmen"""
            x_pos = self.width / data_len * (index + 0.25) + x_offset
            y_pos = self.height / 2 - box_size / 2 + y_offset

            pygame.draw.rect(self.screen, (150, 45, 45), (x_pos, y_pos, box_size, box_size))

            text_surf = self.fonts["large-text"].render(str(val), False, (180, 180, 180))
            self.screen.blit(text_surf, text_surf.get_rect(center=(x_pos + box_size / 2, y_pos + box_size / 2)))

        def draw_boxes(data_copy : Data, exclude_indices : List[int] = []):
            """Funktion som tegner alle firkanter i en datasæt, undtagen de indekser angivet i 'exclude_indices'"""
            for i, val in enumerate(data_copy): 
                if i in exclude_indices: continue
                draw_box(i, val)

        for data_copy, indices in algorithm(data):

            # Løft-op animation
            for t in animate(animation_time):
                self.screen.fill((35, 35, 35))
                draw_boxes(data_copy, indices)

                draw_box(indices[0], data_copy[indices[1]], 0, -t * box_size * 1.2)
                draw_box(indices[1], data_copy[indices[0]], 0, -t * box_size * 1.2)

                pygame.draw.rect(self.screen, (45, 45, 45), (10, 10, 160, 40))
                self.screen.blit(title_surf, (20, 20))
                self.update()

            self.sleep(0.1)

            # Byt-plads animation
            for t in animate(animation_time):
                self.screen.fill((35, 35, 35))
                draw_boxes(data_copy, indices)

                pos0 = self.width / data_len * (indices[0] + 0.25)
                pos1 = self.width / data_len * (indices[1] + 0.25)

                draw_box(indices[0], data_copy[indices[1]], t * (pos1 - pos0), -box_size * 1.2)
                draw_box(indices[1], data_copy[indices[0]], t * (pos0 - pos1), -box_size * 1.2)

                pygame.draw.rect(self.screen, (45, 45, 45), (10, 10, 160, 40))
                self.screen.blit(title_surf, (20, 20))
                self.update()

            self.sleep(0.1)
            
            # Fald-ned animation
            for t in animate(animation_time):
                self.screen.fill((35, 35, 35))
                draw_boxes(data_copy, indices)

                draw_box(indices[0], data_copy[indices[0]], 0, box_size * 1.2 * (-1 + t))
                draw_box(indices[1], data_copy[indices[1]], 0, box_size * 1.2 * (-1 + t))

                pygame.draw.rect(self.screen, (45, 45, 45), (10, 10, 160, 40))
                self.screen.blit(title_surf, (20, 20))
                self.update()
            
            self.sleep(0.8)
