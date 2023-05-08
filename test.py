#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print("hello world","jzq")
#print("请输入:")
# name =input()
# print(name)
# x = 10
# x= x + 5
# print("x: ",x)
# print(len("abc"))
# print(len("焦六六"))

# if语句
# age = 20
# if age > 18:
#     print("成年人")
# elif age > 6:
#     print("青年")
# else:
#     print("未成年")

# #循环
# sum = 0
# testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in testList:
#     sum = sum + x
# print("1..10",sum)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print("1..100",sum)


# sum = 0
# n = 100
# while n > 0:
#     sum = sum + n
#     n = n - 1
# print("while ",sum)

# 定义函数

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print("定义函数",my_abs(-10))

#切片

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print("切片",L[0:2])
# 切片 ['Michael', 'Sarah']

#打印 map

# d = {'a': 1, 'b': 2, 'c': 3}
# for k,v in d.items():
#     print(k,v)

#列表生成式

# testJJ = [x for x in range(1, 11) if x % 2 == 0]
# print("列表生成式",testJJ)

# testStr = ['Hello', 'World', 18, 'Apple', None]
# resultStr = [x.lower() for x in testStr if isinstance(x,str)]
# print(resultStr)

# 高阶函数

# def add(x, y, f):
#     return f(x) + f(y)

# print(add(-5, 6, abs))

# testName = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(testName, key=str.lower))
# #['about', 'bob', 'Credit', 'Zoo']

# #lambda

# f = lambda x: x * x
# print(f(10))

# L = list(filter(lambda n:n % 2 == 1,range(1,20)))
# print(L)

# 模块
#import sys
#print("python运行的环境:",sys.path)

# import sys
# sys.path.append("c:/code/pythonCode/")
# from student import Student

# aStu = Student("jzq",48)
# aStu.print_score()

# from student import add
# print(add(1,2))

# print(dir(aStu))

#文件读写

# with open('./io.txt', 'r') as tempFile:
#     print(tempFile.read())

# with open('c:/code/pythonCode/io.txt', 'a') as tempFile:
#     tempFile.write('\n123456')

#import os

# 查看当前目录的绝对路径:
#print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
#print(os.path.join(os.path.abspath('.'), 'testdir'))

# # 然后创建一个目录:
#os.mkdir(os.path.join(os.path.abspath('.'), 'testdir'))
# # 删掉一个目录:
# os.rmdir(os.path.join(os.path.abspath('.'), 'testdir'))

#拆分路径  后一部分总是最后级别的目录或文件名
#print(os.path.split('c:/code/pythonCode/io.txt'))

# 对文件重命名:
#os.rename('test.txt', 'test.py')
# 删掉文件:
#os.remove('test.py')

#列出当前目录下的所有目录:

# tempFile = [x for x in os.listdir('.') if os.path.isdir(x)]
# print(tempFile)

#列出所有的.py文件

# tempFile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print(tempFile)


#多线程

# import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

import time, threading

allSize = 499086

def download(sizeInfo):
    print(sizeInfo)
    #print("开始下载 {0} {1}-{2}".format(sizeInfo[0],sizeInfo[1],sizeInfo[2]))

def downloadInfo(allSize):
    chunk = 5
    surplusSize = allSize%chunk
    everySize = (allSize -surplusSize) / 5
    
    finalChunk = chunk + 1
    print(surplusSize)
    print(chunk)

    threads = []
    sizeInfo = [0,0,0]

    for x in range(1,int(finalChunk)):
        sizeInfo[0] = x
        sizeInfo[1] = (x-1)*everySize
        sizeInfo[2] = x*everySize -1
        
        t = threading.Thread(target=download, args=(sizeInfo,))
        t.start()
        threads.append(t)

    sizeInfo[0] = finalChunk
    sizeInfo[1] = allSize-surplusSize
    sizeInfo[2] = allSize
    #最后一部分
    t = threading.Thread(target=download, args=(sizeInfo,))
    t.start()
    threads.append(t)

    for t in threads:
        t.join()

downloadInfo(allSize)

import os

# def mergeFile(fileName):
#     path = "./temp"        # 文件夹目录
#     files = os.listdir(path)     # 得到文件夹下的所有文件名称

#     finalFile = open(path+"/"+fileName, 'a+b')  # 以追加模式打开文件

#     for file in files:  # 遍历文件
#         tempFile = open(path+"/"+file,'rb')  # 将打开的文件内容保存到变量f
#         finalFile.write(tempFile.read())                     # 写入文件
#         print(file + ' 文件已经合并：')
#         tempFile.close()
#         os.remove(path+"/"+file)
    
#     finalFile.close()

#     print(fileName,"合并完成")

# mergeFile("xx.jpg")