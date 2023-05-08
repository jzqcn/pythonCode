#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

import sys
import time
import pygame
import random
from myFont import MyFont
from mySprite import MySprite

def test():
    WIDTH = 1200
    HEIGHT = 900
    FPS = 60

    # define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()


    all_sprites = pygame.sprite.Group()
    player = MySprite("./pic/test3.png",(600,450),WHITE)
    print(player.rect)
    all_sprites.add(player)


    # Game loop
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type ==pygame.KEYDOWN:
            # 打印按键的英文字符
                print('键盘按下',event.key)
            if event.type == pygame.KEYUP:
                print('键盘弹起')

        all_sprites.update()

        screen.fill(BLACK)

        all_sprites.draw(screen)

        fpsFont = MyFont(clock.get_fps(),25)
        fpsFont.pos =(15,15)
        screen.blit(fpsFont.render(),fpsFont.pos)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

 


if __name__=='__main__':
    test()
    
