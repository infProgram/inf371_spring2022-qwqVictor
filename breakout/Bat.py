import pygame
from ImageSprite import ImageSprite

class Bat(ImageSprite):
    speed: int
    window_width: int
    window_height: int
    def __init__(self, window: pygame.Surface, speed: int=4):
        ImageSprite.__init__(self, "bat.png")
        self.speed = speed
        self.window_width = window.get_width()
        self.window_height = window.get_height()
        self.rect.bottom = self.window_height
        self.rect.left = (self.window_width - self.image.get_width()) / 2

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

    def move_right(self):
        if self.rect.right < self.window_width:
            self.rect.move_ip(self.speed, 0)
    
    def event_handle(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left()
            elif event.key == pygame.K_RIGHT:
                self.move_right()