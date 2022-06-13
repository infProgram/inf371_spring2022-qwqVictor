import pygame
class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image_file: str):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/' + image_file).convert()
        self.rect = self.image.get_rect()

class MatricedImageSprite(ImageSprite):
    def __init__(self, image_file: str, coordinate: tuple[int], margin: tuple[int], base_offset: tuple[int]):
        ImageSprite.__init__(self, image_file)
        x, y = coordinate
        margin_x, margin_y = margin
        offset_x, offset_y = base_offset
        self.rect.x = x * (self.rect.width + margin_x) + offset_x
        self.rect.y = y * (self.rect.width + margin_y) + offset_y
