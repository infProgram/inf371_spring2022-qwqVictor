#!/usr/bin/env python3
import sys
import pygame
from Ball import Ball
from Bat import Bat
from Brick import Brick
from HPHeart import HPHeartFulfilled, HPHeartLost

pygame.init()
pygame.key.set_repeat(1, 5)
window_size = (640, 480)
window = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Breakout! by Victor")
background_color = (0, 0, 0)
white = (0xff, 0xff, 0xff)
pink = (0xfb, 0x72, 0x99)
purple = (0xff, 0, 0xff)
cyan = (0, 0xff, 0xff)
heading_top = 30
max_hp = 3

def heading(window: pygame.Surface, score: int, hp: int):

    pygame.draw.line(window, white, (0, heading_top), (window_size[0], heading_top))

    def heading_text(content: str, color: tuple[int], x_pos_expr: str, y_pos_expr: str="(heading_top - rect.height) / 2", font_size: int=28, font_family: str=None):
        text = pygame.font.Font(font_family,font_size).render(content, True, color)
        rect = text.get_rect()
        rect.left = eval(x_pos_expr)
        rect.top = eval(y_pos_expr)
        window.blit(text, rect)
        return (rect.x, rect.y, rect.width, rect.height)

    breakout_pos = heading_text("BREAKOUT", purple, "(window_size[0] - rect.width * 1.5) / 2")
    heading_text("by Victor", pink, str(breakout_pos[0] + breakout_pos[2]), font_size=16, y_pos_expr="(%d-rect.height)" % (breakout_pos[1] + breakout_pos[3]))
    heading_text(str(score), cyan, "window_size[0] - rect.width")

    hp_sprites = pygame.sprite.Group()
    for i in range(0, max_hp):
        if i < hp:
            hp_sprites.add(HPHeartFulfilled((i, 0)))
        else:
            hp_sprites.add(HPHeartLost((i, 0)))
    hp_sprites.draw(window)

def main():
    all_sprites = pygame.sprite.Group()
    bouncable_sprites = pygame.sprite.Group()
    bat = Bat(window, speed=2)
    ball = Ball(window, speed_x=2, speed_y=-2, spawn_pos=(window_size[0] / 2, bat.rect.height), head_y=30)
    all_sprites.add(bat, ball)
    bouncable_sprites.add(bat)
    hp = 3
    score = 0
    bonus = 1
    won = False

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
            if won:
                print('Congratulations!',"Congratulations, you won!\nYour score: %d" % (score))
                running = False
                break
            if ball.rect.y > window_size[1]:
                hp -= 1
                if hp < 0:
                    print('Sorry!',"Oh, you lose.\nTake another chance!\nYour score: %d" % (score))
                    running = False
                    break
                else:
                    ball.respawn()
            bounce = pygame.sprite.spritecollide(ball, bouncable_sprites, False)
            if bounce:
                hit_rect = bounce[0].rect
                if hit_rect.left > ball.rect.left or ball.rect.right < hit_rect.right:
                    ball.speed_y *= -1
                else:
                    ball.speed_x *= -1

                if not pygame.sprite.collide_rect(ball, bat):
                    for brick in bounce:
                        score += bonus
                        bonus += 1
                        all_sprites.remove(brick)
                        bouncable_sprites.remove(brick)
                    if len(bouncable_sprites.sprites()) == 1:
                        won = True
                        score += hp * 360
                else:
                    bonus = 1

            window.fill((background_color))
            heading(window, score, hp)
            all_sprites.draw(window)
            all_sprites.update()
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()