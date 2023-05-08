import requests,time, threading,os,sys

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://img.crawler.qq.com/lolwebschool/0/JAutoCMS_LOLWeb_d022041aac79353f50cd4cbb26edef59/0"



allSize = 42403430

print('文件大小 {0:.3f}MB'.format(allSize/(1024*1024)))

print("")
print("")
print("")

def mergeFile(fileName):
    path = "./temp"        # 文件夹目录
    files = os.listdir(path)     # 得到文件夹下的所有文件名称

    finalFile = open(path+"/"+fileName, 'a+b')  # 以追加模式打开文件

    for file in files:  # 遍历文件
        tempFile = open(path+"/"+file,'rb')  # 将打开的文件内容保存到变量f
        finalFile.write(tempFile.read())                     # 写入文件
        print(file + ' 文件已经合并：')
        tempFile.close()
        os.remove(path+"/"+file)
    
    finalFile.close()

    print(fileName,"合并完成")

print("开始下载文件")

downLoadFileName = "test.jpg"


def download(sizeInfo):
    newSizeInfo = sizeInfo[:]
    newSizeInfo[0] = int(newSizeInfo[0])
    newSizeInfo[1] = int(newSizeInfo[1])
    newSizeInfo[2] = int(newSizeInfo[2])
    
    headers_2 = {
    'User-Agent':header["User-Agent"],
    'Range': 'bytes={0}-{1}'.format(newSizeInfo[1],newSizeInfo[2]) #每一个线程的大小 B
    }

    print(headers_2["Range"])

    res_file = requests.get(url, headers=headers_2)
    res_file.encoding = 'GBK'
    if res_file.status_code == 206:
        print("{0}开始下载文件".format(newSizeInfo[0]))
        #保存

        with open("./temp/tempDownFile_{0}".format(int(newSizeInfo[0])),'wb') as downFile:
            downFile.write(res_file.content)

        print(newSizeInfo[0],"写入完成")
    else:
        print("{0}请求文件失败".format(newSizeInfo[0]))
        print("失败码:",res_file.status_code)
        print("请求文件头文件信息",res_file.headers)

def downloadInfo(allSize):
    chunk = 5
    surplusSize = allSize%chunk
    everySize = (allSize -surplusSize) / chunk
    finalChunk = chunk + 1

    threads = []
    sizeInfo = [0,0,0]

    for x in range(1,int(finalChunk)):
        sizeInfo[0] = x
        sizeInfo[1] = (x-1)*everySize
        sizeInfo[2] = x*everySize -1
        
        t = threading.Thread(target=download, args=(sizeInfo))
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
    
    #print("开始合并文件")
    #mergeFile(downLoadFileName)

downloadInfo(allSize)

