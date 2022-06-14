import pygame
import random
from ImageSprite import ImageSprite

class Ball(ImageSprite):
    window_width: int
    window_height: int
    spawn_pos: tuple[int]
    spawn_speed: float
    speed_x: float
    speed_y: float
    head_y: int
    def __init__(self, window: pygame.Surface, speed: float, spawn_pos: tuple[int], head_y: int=0):
        ImageSprite.__init__(self, "ball.png")
        self.window_width = window.get_width()
        self.window_height = window.get_height()
        self.spawn_pos = spawn_pos
        self.spawn_speed = speed
        self.head_y = head_y
        self.respawn()

    def respawn(self):
        self.rect.bottom = self.window_height - self.spawn_pos[1]
        self.rect.left = self.spawn_pos[0]
        factor = 0
        while factor < 0.3 or factor > 0.7:
            factor = random.random()
        self.speed_x = factor * self.spawn_speed
        self.speed_y = -(self.spawn_speed ** 2 - self.speed_x ** 2) ** (1/2)

    def set_speed(self, speed_x: float=None, speed_y: float=None, multiply_mode: bool=False):
        if speed_x != None:
            if multiply_mode:
                self.speed_x *= speed_x
            else:
                self.speed_x = speed_x
            self.speed_y = self.speed_y / abs(self.speed_y) * abs(self.spawn_speed ** 2 - abs(self.speed_x) ** 2) ** (1/2)
        if speed_y != None:
            if multiply_mode:
                self.speed_y *= speed_y
            else:
                self.speed_y = speed_y
            self.speed_x = self.speed_x / abs(self.speed_x) * abs(self.spawn_speed ** 2 - abs(self.speed_y) ** 2) ** (1/2)

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)

        if self.rect.x > self.window_width - self.image.get_width() or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y < self.head_y:
            self.speed_y *= -1