#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ast import Not
import os,shutil

file_1 = []
file_2 = []

for x in os.listdir("C:/CloudMusic/jzq"):
    file_1.append(os.path.splitext(x)[0])

for x in os.listdir("C:/CloudMusic/VipSongsDownload"):
    file_2.append(os.path.splitext(x)[0])

print(len(file_1))

print("第二个文件大小")

print(len(file_2))

# def findFile(f,files):
#     for x in files:
#         if(x == f):
#             return True
#     return False

# for x in os.listdir("C:/CloudMusic/jzq"):
#     file_1.append(os.path.splitext(x)[0])


# for x in os.listdir("C:/CloudMusic/VipSongsDownload"):
#     fuck = os.path.splitext(x)[0]
#     if(findFile(fuck,file_1)):
#         pass
#     else:
#         file_2.append(fuck)


# for x in file_2:
#     name_1 = os.path.join("C:\CloudMusic\VipSongsDownload",x+".ncm")
#     #print(name_1)
#     shutil.move(name_1,"C:\CloudMusic\\aajzq")

# fileName = os.path.join("C:\code\pythonCode","err.txt")

# print(fileName)

# shutil.move(fileName,"C:\code\pythonCode\pic")


    


#print(file_1[0])
#print(type(file_1[0]))