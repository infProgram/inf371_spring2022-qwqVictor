#!/usr/bin/env python3
import sys
from cv2 import line
import pygame
from Ball import Ball
from Bat import Bat
from Brick import Brick

pygame.init()
pygame.key.set_repeat(1, 5)
window_size = (640, 480)
window = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)
heading_top = 30
clock = pygame.time.Clock()

def heading(window: pygame.Surface):

    pygame.draw.line(window, (0xfb, 0x72, 0x99), (0, heading_top), (window_size[0], heading_top))

def main():
    all_sprites = pygame.sprite.Group()
    bouncable_sprites = pygame.sprite.Group()
    bat = Bat(window, speed=2)
    ball = Ball(window, speed_x=2, speed_y=-2, spawn=(window.get_width() / 2, bat.rect.height), head_y=30)
    all_sprites.add(bat, ball)
    bouncable_sprites.add(bat)
    score = 0

    for i in range(1, 12+1):
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
            bounce = pygame.sprite.spritecollide(ball, bouncable_sprites, False)
            if bounce:
                hit_rect = bounce[0].rect
                if hit_rect.left > ball.rect.left or ball.rect.right < hit_rect.right:
                    ball.speed_y *= -1
                else:
                    ball.speed_x *= -1

                if not pygame.sprite.collide_rect(ball, bat):
                    score += len(bounce)
                    for brick in bounce:
                        all_sprites.remove(brick)
                        bouncable_sprites.remove(brick)

            window.fill((background_color))
            heading(window)
            all_sprites.draw(window)
            all_sprites.update()
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()