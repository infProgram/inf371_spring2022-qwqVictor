import sys
from time import sleep
import pygame
from item import Item

pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)

shark_ball = Item(picture_path="shark_ball.png", picture_size=(80, 80), window_size=window_size, speed=(4, 4))
spider_ball = Item(picture_path="spider_ball.png", picture_size=(80, 80), window_size=window_size, speed=(5, 5))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("user exit", file=sys.stderr)
            running = False
            break
    if running:
        screen.fill((background_color))
        shark_ball.move()
        shark_ball.collide(spider_ball, (-1, 1))
        shark_ball.blit(screen)
        spider_ball.move()
        spider_ball.collide(shark_ball, (-1, 1))
        spider_ball.blit(screen)
        pygame.display.flip()
        sleep(1/120)

pygame.quit()