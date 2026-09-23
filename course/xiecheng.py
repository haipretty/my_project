import json

##yield生成器
def consumer():
    print("消费者启动")
    while True:
        data = yield          # ← 暂停在这里，等待外部 send 数据
        print(f"消费者收到: {data}")

def producer(c):
    next(c)                   # 先预激（prime）协程，让它跑到第一个 yield
    for i in range(3):
        print(f"生产者发送: {i}")
        c.send(i)             # 给协程传数据
    c.close()                 # 关闭协程

# 运行
c = consumer()                  #不执行consumer函数，只是创建生成器对象
producer(c)


##三方协程
"""
monkey.patch_all()	替换标准库阻塞调用
gevent.spawn(func, *args)	启动一个 greenlet 协程
gevent.joinall(jobs)	等待所有协程完成
gevent.sleep(seconds)	非阻塞睡眠（交出控制权）
"""
import gevent
from gevent import monkey
monkey.patch_all()    # ← 猴子补丁，必须放在最前面，且在所有 import 之前

import requests       # 注意：要在 patch 之后 import

def fetch(url):
    print(f"开始下载 {url}")
    resp = requests.get(url, timeout=10)
    print(f"完成 {url}, 长度 {len(resp.text)}")

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

# 创建并发的 greenlet（轻量级线程/协程）
jobs = [gevent.spawn(fetch, url) for url in urls]

# 等待全部完成
gevent.joinall(jobs)
print("全部完成")


##协程
import asyncio

async def download(url):
    await asyncio.sleep(1)                  #遇到异步操作：挂起当前协程，事件循环调度其他任务，1s后返回

async def main():
    #方式1：单个协程
    result = await download(url)            #挂起当前协程，立即调用download协程，完成后返回

    #方式2：并发多个协程
    tasks = [download(url) for url in urls]
    results = await asyncio.gather(*tasks)  #按传入的tasks顺序返回结果列表

    #方式3：后台任务
    task = asyncio.create_task(download())  #包装成task提交给事件循环，当前协程继续执行
    result = await task                     #挂起当前协程，等待task完成返回
    
    #方式4：设置什么时候返回
    done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)  #任意一个task完成就返回

    #方式5： 运行同步函数
    """
    同步库：pandas/scikit-learn/requests不能用await，丢到线程池
    异步库：aiohttp/aiofiles并发下载数据，aiomysql并发数据库查询，可以用await
    """
    loop = asyncio.get_running_loop()       #正在运行的事件循环对象
    result = await loop.run_in_executor(None, heavy_compute, 5) #在线程池中运行同步函数

main = main()		    #协程函数：不会立即执行，而是返回协程对象
asyncio.run(main)       #启动事件循环

## 实际应用：并发下载数据
import aiohttp      #异步http

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()        #异步操作：事件循环调度其他任务

async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]   #创建多个任务
        results = await asyncio.gather(*tasks)      #并发执行多个协程
        
        for url, html in zip(urls, results):
            print(f"{url}: {len(html)} bytes")

asyncio.run(main())     #启动事件循环


