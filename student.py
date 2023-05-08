#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'


# https://www.liaoxuefeng.com/

def add(a,b):
    return a+b

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

        #private
        self.__money = 0
        #强制访问 aStu._Student__money

    def setMoney(self,num):
        self.__money = num

    def getMoney(self):
        return self.__money

    def print_score(self):
        print('%s: %s' % (self.name, self.score))



if __name__=='__main__':
    #如果这是主运行文件则执行下面的代码，如果是被别人调用则忽略
    aStu = Student("jzq",38)

    aStu.print_score()