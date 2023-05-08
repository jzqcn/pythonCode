#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
import pygame

__author__ = 'jzq'

class MyFont(object):
    def __init__(self, txt = "None txt",fontSize = 30, color = (255, 255, 255)):
       self.__txt = str(txt)
       self.__color = color
       self.__fontSize = fontSize
       self.__pos = (0,0)

    def print_info(self):
        print('%s: %s :%s' % (self.__txt, self.__color,self.__fontSize))


    @property
    def txt(self):
        return self.__txt
    
    @txt.setter
    def txt(self, value):
        self.__txt = str(value)

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def fontSize(self):
        return self.__fontSize
    
    @fontSize.setter
    def fontSize(self, value):
        self.__fontSize = value

    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self, value):
        self.__pos = value

    def render(self):
        if self.__fontSize == None:
            self.__fontSize = 30
        if self.__color == None:
            self.__color = (255, 255, 255)
        if self.__txt == None:
            self.__txt = "None txt"
        renderFont = pygame.font.Font(None,self.__fontSize)
        return renderFont.render(self.__txt, True, self.__color)

def test():
    pass
if __name__=='__main__':
    test()
    