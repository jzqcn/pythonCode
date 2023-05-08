import requests
import re
import threading
import time

# 获取json数据
def getApiJSON(url,headers):
    try:
        print('获取JSON数据!')
        res = requests.get(url,headers=headers)
        print('获取JSON数据成功!')
    except:
        print('获取JSON数据失败!')
        return getApiJSON(url,headers)
    JSON_data = res.json()
    print("JSON_data: ",JSON_data)
    return JSON_data

# 进行图片下载
def download(url, pid, way):
    global errCount
    res = requests.get(url)
    try:
        content = res.content
    except:
        print('下载图片失败!')
        print(res.headers)
        lock.acquire()
        errCount += 1
        lock.release()
        with open ('err.txt',"a") as file :
            file.write(setu_url+'\n')
        return
    with open("./pic/"+pid +"."+way, "wb") as file:
        file.write(content)
    print('下载成功一张图片!')

allTime = 0
allSuccess = 0

# 每次循环下载100张图
for i in range(1):
    print(f'第 {i+1} 张!')
    url = 'https://api.lolicon.app/setu/v2?num=1&r18=1&size=original'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    lock = threading.Lock()
    threads = []
    errCount = 0
    startTime = time.time()
    jsons = getApiJSON(url, headers)
    jsons = jsons['data']

    for json in jsons:
        setu_url = json['urls']['original']
        setu_pid = str(json['pid'])
        way = str(json["ext"])
        print("url ",setu_url)
        print("setu_pid ",setu_pid)
        #print("way ",way)
        t = threading.Thread(target=download, args=(setu_url,setu_pid,way,))
        t.start()
        threads.append(t)
        time.sleep(1)

    for t in threads:
        t.join()
        print(f'线程{t.name} 完成!')

    endTime = time.time()
    print(f'第 {i+1} 次完成 ! 费时 {endTime-startTime}! 下载 {100-errCount} 成功!')
    allTime += endTime - startTime
    allSuccess += 100 - errCount
    time.sleep(1)

print(f"全部下载完成! 费时 {allTime}! 下载 {allSuccess} 成功!")
