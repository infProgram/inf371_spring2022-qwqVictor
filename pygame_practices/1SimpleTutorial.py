import sys
import pygame
import random

pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
speed = [10, 10]
radius = 25
background_color = (0, 0, 0)
ball_color = (0xfb, 0x72, 0x99)
ball = pygame.Surface((radius * 2, radius * 2))
ball_rect = pygame.draw.circle(ball, ball_color, (radius, radius), radius).move((random.randint(radius, window_size[0] - radius), random.randint(radius, window_size[1] - radius)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("user exit", file=sys.stderr)
            running = False
            break
    if running:
        ball_rect = ball_rect.move(*speed)
        if ball_rect.left <= 0 or ball_rect.right >= window_size[0]:
            speed[0] = -speed[0]
        if ball_rect.top <= 0 or ball_rect.bottom >= window_size[1]:
            speed[1] = -speed[1]
        screen.fill((background_color))
        screen.blit(ball, ball_rect)
        pygame.display.flip()

pygame.quit()