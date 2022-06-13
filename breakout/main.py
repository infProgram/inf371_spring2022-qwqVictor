#!/usr/bin/env python3
import sys
import pygame

def main(argv: "list[str]"):
    size = width, height = 640, 480
    pygame.init()
    window = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    bouncable_sprites = pygame.sprite.Group()
    
    while True:


        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    main(sys.argv)