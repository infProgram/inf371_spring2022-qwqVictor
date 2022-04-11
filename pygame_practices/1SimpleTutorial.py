import sys
from time import sleep
import pygame
import random

pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
background_color = (0, 0, 0)
pink_color = (0xfb, 0x72, 0x99)
blue_color = (59, 181, 243)

class Ball:

    def __init__(self, color: tuple[int], radius: int, window_size: tuple[int], speed: tuple[int]):
        self.speed = [x for x in speed]
        self.window_size = window_size
        self.ball = pygame.Surface((radius * 2, radius * 2))
        self.ball_rect = pygame.draw.circle(self.ball, color, (radius, radius), radius).move((random.randint(radius, window_size[0] - radius), random.randint(radius, window_size[1] - radius)))

    def move(self):
        self.ball_rect = self.ball_rect.move(*self.speed)
        if self.ball_rect.x <= 0 or self.ball_rect.x >= self.window_size[0]:
            self.speed[0] = -self.speed[0]
        if self.ball_rect.y <= 0 or self.ball_rect.y >= self.window_size[1]:
            self.speed[1] = -self.speed[1]
    
    def blit(self, screen: pygame.Surface):
        screen.blit(self.ball, self.ball_rect)

pink_ball = Ball(color=pink_color, radius=25, window_size=window_size, speed=(10, 10))
blue_ball = Ball(color=blue_color, radius=20, window_size=window_size, speed=(12, 12))

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