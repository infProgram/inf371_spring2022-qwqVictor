import sys
import pygame

pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

ball = pygame.Surface((50, 50))
ball_rect = pygame.draw.circle(ball, (0xfb, 0x72, 0x99), (25, 25), 25)

screen.blit(ball, ball_rect)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("user exit", file=sys.stderr)
            running = False
            break
    if running:
        pass

pygame.quit()