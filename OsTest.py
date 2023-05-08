
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

import os,sys


def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

    print("================================")
    print(os.name)

    print(os.getcwd())

    print(os.listdir("./pic"))

    pathTest = "./pic/err.txt"
    pathName = "./pic/err"
#返回文件路径
    print(os.path.dirname(pathTest))

#返回该文件所在的母目录
    os.path.basename(pathTest)

#将目录和文件名分开
    print(os.path.split(pathName))

#连接目录和文件名
    print(os.path.join("./pic", "err.txt"))


if __name__=='__main__':
    test()
    