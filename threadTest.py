import threading
import time

event = threading.Event()

def loop():
    n = 0
    while n < 5:
        n += 1
        print("i am loop")
        time.sleep(1)
    event.set()

t = threading.Thread(target=loop, name='LoopThread')
t.start()

while not event.is_set():
    time.sleep(1)
    print("等待子线程完成")

print("退出循环，任务完成")

t.join()