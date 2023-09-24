import pygame
import sys
import time

import array

from consts import Data, DataSorter, Size

my_font_title = None
my_font = None

class Visualizer:
    def __init__(self, title : str = "Sketch", size : Size = (600, 600)) -> None:
        """Initializes the Visualizer and pygame"""
        self.width, self.height = size

        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        global my_font, my_font_title
        my_font_title = pygame.font.SysFont("arialblack", 30)
        my_font = pygame.font.SysFont("calibri", 25)

    def quit(self) -> None:
        """Exits the Visualizer and terminates pygame"""
        pygame.quit()
        sys.exit(0)
    
    def update(self) -> None:
        if pygame.event.peek(eventtype = pygame.QUIT): self.quit()
        self.clock.tick()
        pygame.display.flip()

    def sleep(self, num_seconds : float) -> None:
        """Halts the Visualizer for 'num_seconds' seconds"""
        if num_seconds <= 0:
            self.update()
            return
        start_time = time.time()
        while time.time() - start_time < num_seconds: self.update()

    def halt(self):
        while True: self.update()

    def await_press(self, key : str = ""):
        while True:
            for event in pygame.event.get(eventtype = pygame.KEYDOWN):
                if pygame.key.name(event.key).lower() == key.lower(): return
            self.update()

    def bar_animation(self, algorithm : DataSorter, data : Data, title : str = "", time_interval : float = 0.01) -> None:
        """..."""
        last_data_copy = None
        
        text_surface_title = my_font_title.render(title, False, (180, 180, 180))
        text_surface = my_font.render(f"n = {len(data)}", False, (180, 180, 180))

        for data_copy, indices in algorithm(data):
            self.screen.fill(color = (35, 35, 35))

            for j, val in enumerate(data_copy):
                w, h = self.width / len(data_copy), self.height * val
                color = (170, 40, 40) if j in indices else (90, 90, 90)
                pygame.draw.rect(surface = self.screen, color = color, rect = (w * j, self.height - h, w, h))
            
            self.screen.blit(text_surface_title, (20, 20))
            self.screen.blit(text_surface, (20, 60))

            self.sleep(time_interval)
            last_data_copy = data_copy

        for i in range(len(last_data_copy)):

            self.screen.fill(color = (35, 35, 35))
            
            for j, val in enumerate(last_data_copy):
                w, h = self.width / len(last_data_copy), self.height * val
                color = (40, 170, 40) if i >= j else (90, 90, 90)
                pygame.draw.rect(surface = self.screen, color = color, rect = (w * j, self.height - h, w, h))

            self.screen.blit(text_surface_title, (20, 20))
            self.screen.blit(text_surface, (20, 60))
            self.sleep(1 / len(last_data_copy))
