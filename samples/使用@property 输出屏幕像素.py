# @迷茫的老九:如果不加私有变量符号_为什么会显示递归错误？
# @廖老师：函数名就是变量，不要重。当你引用self.height时你就引用了height这个函数
class Screen(object):
    def isint(self, px):
        if not isinstance(px, int):
            raise ValueError('px must be an integer!')
        if px < 0:
            raise ValueError('px must be an positive integer!')

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self.isint(value)
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self.isint(value)
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
