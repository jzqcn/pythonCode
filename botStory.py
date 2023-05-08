#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

import sys

import random

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def Unicode():
	val = random.randint(0x4e00, 0x9fbf)
	return chr(val)

# 对于第55区，D7FA-D7FE的5个是没有编码的，需要在两个字节组合的范围中特意剔除一下

# 215 250 -- 215 254
def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str

def getWordIndex(index):
    head = 176   #random.randint(176, 247)
    body = 161 + index #random.randint(161, 254)

    head = head + (index // 94)
    body = 161 + (index % 94)
    if (head == 215) or (head > 247):
        str = ""
        print("这个字不存在")
    else:
        val = f'{head:x}{body:x}'
        str = bytes.fromhex(val).decode('gb2312')
    return str


if __name__=='__main__':
    test()
    word = []
    for w in range(10):
        word.append(getWordIndex(w+180))


    for outWord in word:
        print(outWord)

