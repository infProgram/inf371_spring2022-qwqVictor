import sys
import pygame
import random

pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
speed = (10, 10)
radius = 25
background_color = (0, 0, 0)
ball_color = (0xfb, 0x72, 0x99)

class Ball:

    def __init__(self, color: tuple[int], radius: int, window_size: tuple[int], speed: tuple[int]):
        self.speed = [x for x in speed]
        self.window_size = window_size
        self.ball = pygame.Surface((radius * 2, radius * 2))
        self.ball_rect = pygame.draw.circle(self.ball, color, (radius, radius), radius).move((random.randint(radius, window_size[0] - radius), random.randint(radius, window_size[1] - radius)))

    def move(self):
        self.ball_rect = self.ball_rect.move(*self.speed)
        if self.ball_rect.left <= 0 or self.ball_rect.right >= self.window_size[0]:
            self.speed[0] = -self.speed[0]
        if self.ball_rect.top <= 0 or self.ball_rect.bottom >= self.window_size[1]:
            self.speed[1] = -self.speed[1]
    
    def blit(self, screen: pygame.Surface):
        screen.blit(self.ball, self.ball_rect)

pinkBall = Ball(ball_color, radius, window_size, speed)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("user exit", file=sys.stderr)
            running = False
            break
    if running:
        screen.fill((background_color))
        pinkBall.move()
        pinkBall.blit(screen)
        pygame.display.flip()

pygame.quit()