import asyncio
import time

async def hello():
    print('Hello world_1')
    await asyncio.sleep(2)
    print('Hello again_1')

async def hello2(finish_event, lock):
    print('Hello world_2')
    await asyncio.sleep(2)
    print('Hello again_2')

    async with lock:
        global finish
        finish = True
        finish_event.set()

async def test():
    finish_event = asyncio.Event()
    lock = asyncio.Lock()
    tasks = []
    tasks.append(asyncio.create_task(hello()))
    tasks.append(asyncio.create_task(hello2(finish_event, lock)))
    tasks.append(finish_event.wait())

    while not finish:
        print("主线程循环")
        await asyncio.sleep(0.5)

    await asyncio.gather(*tasks)

finish = False
loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
