import pygame
from ImageSprite import ImageSprite

class Ball(ImageSprite):
    window_width: int
    window_height: int
    spawn_pos: tuple[int]
    spawn_speed: tuple[int]
    speed_x: int
    speed_y: int
    head_y: int
    def __init__(self, window: pygame.Surface, speed_x: int, speed_y: int, spawn_pos: tuple[int], head_y: int=0):
        ImageSprite.__init__(self, "ball.png")
        self.window_width = window.get_width()
        self.window_height = window.get_height()
        self.spawn_pos = spawn_pos
        self.spawn_speed = (speed_x, speed_y)
        self.head_y = head_y
        self.respawn()

    def respawn(self):
        self.rect.bottom = self.window_height - self.spawn_pos[1]
        self.rect.left = self.spawn_pos[0]
        self.speed_x, self.speed_y = self.spawn_speed

    def update(self):
        self.rect = self.rect.move(self.speed_x, self.speed_y)

        if self.rect.x > self.window_width - self.image.get_width() or self.rect.x < 0:
            self.speed_x *= -1
        if self.rect.y < self.head_y:
            self.speed_y *= -1