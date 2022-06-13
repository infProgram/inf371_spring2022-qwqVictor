import pygame
from ImageSprite import ImageSprite

class Brick(ImageSprite):
    def __init__(self, coordinate: tuple[int], margin: tuple[int]=(5, 2), base_offset: tuple[int]=(40, 50)):
        ImageSprite.__init__("brick.png")
        x, y = coordinate
        margin_x, margin_y = margin
        offset_x, offset_y = base_offset
        self.rect.x = x * (self.rect.width + margin_x) + offset_x
        self.rect.y = y * (self.rect.width + margin_y) + offset_y
