
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

import os,sys,shutil


def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

    print("================================")
    selfFile = sys.argv[0]
    
    print(selfFile)
    selfPathAndFile = os.path.split(selfFile)

    selfPath = selfPathAndFile[0]

    currentFile = selfPathAndFile[1]

    fileNames = os.path.splitext(currentFile)

    fileName = fileNames[0]

    fileNameZui = fileNames[1]

    count = 1

    fileNameLen = len(fileName)

    writeFile = fileName[0:(fileNameLen - 2)]

    newName = ""

    while True:
        newName = selfPath + "/" + writeFile + "_" +str(count) +fileNameZui
        if os.path.exists(newName):
            count = count + 1
            print(newName)
        else:
            break

    print(newName)

    shutil.copy(selfFile,newName)

    # with open(selfFile, 'r') as f:
    #     fileContent = f.read()

    # with open(newName, 'w') as f:
    #     f.write(fileContent)



 

if __name__=='__main__':
    test()
    