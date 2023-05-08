import requests

url = "http://127.0.0.1:8000/downloadFile"
response = requests.get(url)



# 打印 HTTP 响应头
print('Headers:')
for key, value in response.headers.items():
    print(f'    {key}: {value}')

# 打印 HTTP 状态码
print(f'Status Code: {response.status_code}')

# 打印 HTTP 响应正文的编码方式
print(f'Encoding: {response.encoding}')

# 打印服务器设置的所有 cookie
print('Cookies:')
for cookie in response.cookies:
    print(f'    {cookie.name}: {cookie.value}')

# 打印响应的 URL
print(f'URL: {response.url}')

# 打印发送请求的 PreparedRequest 对象
print(f'Request: {response.request}')

#print(response.cookies['cookie_name'])