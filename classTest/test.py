#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

import sys,hello

from hello import Student
from hello import Dog

def test():
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()

    dog = Dog()
    dog.run()
    dog.eat()


if __name__=='__main__':
    test()
    
