# 1 规范名字
def normalize(name):
    return name[0].upper() + name[1:].lower()
    # return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 2 求积
from functools import reduce


def prod(L):
    def mult(x, y):
        return x * y

    return reduce(mult, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 3 字符串转换成浮点数
from functools import reduce


def str2float(s):
    i = 0;
    dot = 0;
    for i in range(len(s)):
        if s[i] == '.':
            s = s[:i] + s[i + 1:]
            dot = len(s) - i
            break

    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s)) / (10 ** dot)


print('str2float(\'123.456\') =', str2float('123.456'))
