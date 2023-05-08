#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
import pygame

__author__ = 'jzq'

class MySprite(pygame.sprite.Sprite):
    def __init__(self, imagePath,pos = (0,0),colorKey = (0, 0, 0)):
       pygame.sprite.Sprite.__init__(self)
       
       self.image = pygame.image.load(imagePath).convert()
       self.image.set_colorkey(colorKey)
       self.__colorKey = colorKey

       self.__pos = pos

       self.rect = self.image.get_rect()
       self.rect.center = self.__pos

    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self, value):
        self.__pos = value

    @property
    def colorKey(self):
        return self.__colorKey
    
    @colorKey.setter
    def colorKey(self, value):
        self.__colorKey = value
