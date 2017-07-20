import math


def quadratic(a, b, c):
    if a == 0:
        raise TypeError('a is zero', a)
    for i in [a, b, c]:
        if not isinstance(i, (int, float)):
            raise TypeError('bad operand type', i)

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return 'no real roots'
    if delta == 0:
        x1 = -b / (2 * a)
        return 'two equal roots: %.2f' % x1
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2


print(quadratic(1, 1, 1))  # => no real roots
print(quadratic(1, 4, 4))  # => two equal roots: -2.00
print(quadratic(2, 3, 1))  # => (-0.5, -1.0)
print(quadratic(1, 3, -4))  # => (1.0, -4.0)
