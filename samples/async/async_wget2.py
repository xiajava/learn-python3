#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


# http://t.cn/R9yJKlz
async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect  # 这里不是生成器，只负责接收reader、writer
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))  # header编码后写入了writer
    await writer.drain()  # 这里是生成器，这里生成了新的header和body
    while True:
        line = await reader.readline()  # 只读取头部
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
