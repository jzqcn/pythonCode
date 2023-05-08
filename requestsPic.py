import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://img.crawler.qq.com/lolwebschool/0/JAutoCMS_LOLWeb_418f647b0952c1f387ff51c99733d391/0'
res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
if res.status_code == 200:
    print("访问成功")
else:
    print("访问失败")
    print("失败码:",res.status_code)
print("网页的头文件信息",res.headers)

#保存
with open('lolPic.jpg','wb') as fileHtml:
    fileHtml.write(res.content)