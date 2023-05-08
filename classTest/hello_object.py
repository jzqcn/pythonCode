#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

class Student(object):
    __slots__ = ('__name', '__age') # 用tuple定义允许绑定的属性名称

    def __init__(self, name, score):
       self.__name = name
       self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        self.__score = score

def test():
    pass
if __name__=='__main__':
    test()
    