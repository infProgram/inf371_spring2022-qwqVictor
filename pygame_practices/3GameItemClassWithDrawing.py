import sys
from time import sleep
import pygame
from item import DrawCircleItem

pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)

pink_color = (0xfb, 0x72, 0x99)
blue_color = (59, 181, 243)

pink_ball = DrawCircleItem(color=pink_color, radius=25, window_size=window_size, speed=(10, 10))
blue_ball = DrawCircleItem(color=blue_color, radius=20, window_size=window_size, speed=(12, 12))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("user exit", file=sys.stderr)
            running = False
            break
    if running:
        screen.fill((background_color))
        pink_ball.move()
        pink_ball.blit(screen)
        blue_ball.move()
        blue_ball.blit(screen)
        pygame.display.flip()
        sleep(1/120)

pygame.quit()