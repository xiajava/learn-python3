#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @contextmanager 任何对象，只要正确实现了上下文管理，就可以用于with语句
from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

# http://t.cn/R9vG3VC
@contextmanager
def loging(title, msg):
    print('Loging begin with {title}:{msg}'.format(title=title, msg=msg))
    yield
    print('Loging end with {title}:{msg}'.format(title=title, msg=msg))


if __name__ == '__main__':
    with loging('test', 'some message') as l:
        print('do something')

# @closing 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://xiajava.github.io/')) as page:
    for line in page:
        print(line)


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
