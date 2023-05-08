
import os
def mergeFile(filePath,fileName):      # 文件夹目录
    files = os.listdir(filePath)     # 得到文件夹下的所有文件名称

    finalFile = open(filePath+"/"+fileName, 'a+b')  # 以追加模式打开文件

    for file in files:  # 遍历文件
        tempFile = open(filePath+"/"+file,'rb')  # 将打开的文件内容保存到变量f
        finalFile.write(tempFile.read())                     # 写入文件
        print(file + ' 文件已经合并：')
        tempFile.close()
        os.remove(filePath+"/"+file)
    
    finalFile.close()

    print(fileName,"合并完成")

filePath = "./temp"  
fileName = "lol.jpg"
mergeFile(filePath,fileName)