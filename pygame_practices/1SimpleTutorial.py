import sys
import pygame
import random

pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
speed = [10, 10]
ball = pygame.Surface((50, 50))
ball_rect = pygame.draw.circle(ball, (0xfb, 0x72, 0x99), (25, 25), 25).move((random.randint(25, window_size[0] - 25), random.randint(25, window_size[1] - 25)))

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
        screen.fill((0, 0, 0))
        screen.blit(ball, ball_rect)
        pygame.display.flip()

pygame.quit()