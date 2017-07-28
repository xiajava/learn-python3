#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1):
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


# 获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
