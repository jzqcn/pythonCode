import requests,time, threading,os,sys

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://down.qis123.com/txt/qis123/txt3/wanjiexianwang.txt"


headers_2 = {
'User-Agent':header["User-Agent"],
'Range': 'bytes={0}-{1}'.format(0,1024) #每一个线程的大小 B
}

print(headers_2["Range"])

res_file = requests.get(url, headers=headers_2)
#res_file.encoding = 'GBK'
if res_file.status_code == 206:
    print("请求成功")
    print(res_file.headers)
elif res_file.status_code == 200:
    with open("temp.html",'wb') as downFile:
                downFile.write(res_file.content)
else:
    print("失败码:",res_file.status_code)
    print("请求文件头文件信息",res_file.headers)

print("测试完成")
