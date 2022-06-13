import pygame
import os

class SoundEffect(pygame.mixer.Sound):
    def __init__(self, sound_file: str, initial_volume: float=40):
        pygame.mixer.Sound.__init__(self, os.path.join(os.path.dirname(__file__), 'assets', sound_file))
        self.set_volume(initial_volume)