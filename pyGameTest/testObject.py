#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

from myFont import MyFont

if __name__=='__main__':
    fonta = MyFont("hello",(255,0,0),30)

    print(fonta.txt)
    print(fonta.color)
    print(fonta.fontSize)

    fonta.print_info()
    fonta.txt = ("jzq")
    fonta.color = ((255,255,255))
    fonta.fontSize = 60

    print(fonta.txt)
    print(fonta.color)
    print(fonta.fontSize)
    