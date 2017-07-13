# http://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/001489375020168cbc881fbed0a4354ba3c13ef3474d9f2000

class Chain(object):
    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path):
        if path == 'users' or path == 'group':
            return Chain('%s' % (self._path))
        else:
            return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


api = Chain().users('michael').group('student').repos
print(api)
print(callable(api))
