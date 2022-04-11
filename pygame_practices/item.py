import pygame
import random

class Item:
    picture: pygame.Surface
    rect: pygame.Rect
    window_width: int
    window_height: int
    speed: "list[int]"

    def __init__(self, picture_path: str, window_size: tuple[int], speed: tuple[int], position: "tuple[int]" = None, picture_size: tuple[int] = None):
        self.picture = pygame.image.load(picture_path)
        if picture_size:
            self.picture = pygame.transform.scale(self.picture, picture_size)
        self.rect = self.picture.get_rect()
        self.window_width, self.window_height = window_size
        self.speed = list(speed)
        if position:
            self.rect.move_ip(position)
        else:
            self.randomize_position()

    def blit(self, screen: pygame.Surface):
        screen.blit(self.picture, self.rect)

    def move(self):
        self.rect = self.rect.move(*self.speed)
        if self.rect.left <= 0 or self.rect.right >= self.window_width:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0 or self.rect.bottom >= self.window_height:
            self.speed[1] = -self.speed[1]

    def randomize_position(self):
        self.rect.move_ip((random.randint(0, self.window_width), random.randint(0, self.window_height)))

class DrawCircleItem(Item):
    def __init__(self, color: tuple[int], radius: int, window_size: tuple[int], speed: tuple[int], position: "tuple[int]" = None):
        self.picture = pygame.Surface((radius * 2, radius * 2))
        self.rect = pygame.draw.circle(self.picture, color, (radius, radius), radius)
        self.rect = self.picture.get_rect()
        self.window_width, self.window_height = window_size
        self.speed = list(speed)
        if position:
            self.rect.move_ip(position)
        else:
            self.randomize_position()