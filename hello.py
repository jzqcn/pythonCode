#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'jzq'

import sys,json,os

def check_config():
    # 检查是否存在配置文件
    if not os.path.exists("pyQt5多线程下载程序的配置文件.json"):
        # 如果不存在，创建一个新的配置文件
        config = {
            "author": "jzq",
            "info": "pyQt5多线程下载程序的信息",
            "defaultDirectory": "D:/soft",
            "header": {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'},
            "url": "https://mksoftcdnhp.mydown.com/642fbdf5/c0e893da2f867d79aa06593883cd8502/uploadsoft/newsoft/QQGame_5.31.57570.0_1080000167_0.exe"
        }
        with open("pyQt5多线程下载程序的配置文件.json", "w") as f:
            json.dump(config, f)
        return config
    else:
        # 如果存在，读取已有的配置文件
        with open("pyQt5多线程下载程序的配置文件.json", "r") as f:
            config = json.load(f)
        return config
    
def test():
   config = check_config()
   print(config)
   #冒泡排序

if __name__=='__main__':
    test()
    