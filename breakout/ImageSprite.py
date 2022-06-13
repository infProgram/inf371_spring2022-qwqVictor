import pygame
class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image_file: str):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/' + image_file).convert()
        self.rect = self.image.get_rect()