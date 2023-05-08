import requests as r
import threading
import time


def download_content(url, filename):
    response = r.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    # start = time.time()
    # for i in range(10):
    #     download_content('https://source.unsplash.com/user/c_v_r/100x100', f'{i}.png')
    # end = time.time()
    # print(f'TIME TAKEN TO DOWNLOAD 10 IMAGES WITHOUT MULTI THREADING: {end - start}')

    start = time.time()
    for i in range(10):
        thread = threading.Thread(target=download_content, args=['https://source.unsplash.com/user/c_v_r/100x100', f'{i}.png'])
        thread.start()
    end = time.time()
    print(f'TIME TAKEN TO DOWNLOAD 10 IMAGES USING MULTI THREADING: {end - start}')
