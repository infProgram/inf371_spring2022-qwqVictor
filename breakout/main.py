#!/usr/bin/env python3
import sys
import pygame
from Ball import Ball
from Bat import Bat
from Brick import Brick

pygame.init()
pygame.key.set_repeat(200, 30)
window_size = (640, 480)
window = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)
clock = pygame.time.Clock()

def main():
    all_sprites = pygame.sprite.Group()
    bouncable_sprites = pygame.sprite.Group()
    bat = Bat(window, speed=30)
    ball = Ball(window, speed_x=2, speed_y=-2, spawn=(window.get_width() / 2, bat.rect.height))
    all_sprites.add(bat, ball)
    bouncable_sprites.add(bat)

    for i in range(1, 6+1):
        for j in range(1, 4+1):
            brick = Brick((i, j))
            all_sprites.add(brick)
            bouncable_sprites.add(brick)

    print("Bootstrapped.")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            bat.event_handle(event)
        if running:
            window.fill((background_color))
            all_sprites.draw(window)
            all_sprites.update()
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()