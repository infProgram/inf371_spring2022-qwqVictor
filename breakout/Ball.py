import pygame
from breakout.ImageSprite import ImageSprite

class Ball(ImageSprite):
    window_width: int
    window_height: int
    speed_x: int
    speed_y: int
    def __init__(self, window: pygame.Surface, speed_x: int, speed_y: int, spawn: tuple[int]):
        ImageSprite(self, "ball.png")
        self.window_width = window.get_width()
        self.window_height = window.get_height()
        self.rect.bottom = self.window_height - spawn[1]
        self.rect.left = spawn[0]
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)

        if self.rect.x > self.window_width - self.image.get_width() or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1