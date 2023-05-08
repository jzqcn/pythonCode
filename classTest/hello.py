#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

import sys

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

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog Eating meat...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
    
    def eat(self):
        print('Cat Eating meat...')

def run_twice(animal):
    animal.run()
    animal.run()

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()

    dog = Dog()
    dog.run()
    dog.eat()
    run_twice(Cat())

if __name__=='__main__':
    test()
    