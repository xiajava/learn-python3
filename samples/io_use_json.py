#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student('Bob', 20, 88)
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)

# 如果要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后传入的object_hook函数负责把dict转换为Student实例
print(json.loads(std_data, object_hook=dict2student))
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print('Load std_data:', rebuild)

'''
Dump Student: {"age": 20, "name": "Bob", "score": 88}
<__main__.Student object at 0x0000025F6D10CEF0>
Load std_data: <__main__.Student object at 0x0000025F6D10CEB8>
'''
