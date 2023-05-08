import requests,time, threading,os,sys

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://down.qis123.com/txt/qis123/txt3/wanjiexianwang.txt"


resp = requests.get(url, headers=header, stream=True)
if 'Content-Length' in resp.headers:
    print("文件总大小 ",resp.headers["Content-Length"])

print("测试完成")
