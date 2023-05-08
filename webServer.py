from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    with open('hello.html', 'r',encoding='utf-8') as f:
        content = f.read()
    return content

@app.route('/downloadFile')
def downloadFile():
    # 获取文件路径和文件名
    file_path = r'D:\soft\testDownloadFile.pdf'
    file_name = file_path.split('\\')[-1]
    # 使用 send_file() 函数将文件发送给用户
    return send_file(file_path, as_attachment=True, download_name=file_name)

if __name__ == '__main__':
  #设置host和port
  app.run(host='127.0.0.1', port=8000)

