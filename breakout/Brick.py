import pygame
from breakout.ImageSprite import ImageSprite

class Brick(ImageSprite):
    def __init__(self, x: int, y: int):
        ImageSprite("brick.png")
        self.rect.x = x
        self.rect.y = y
