def move(n, x, y, z):
    if n == 1:
        print(x, '-->', z)  # 一个盘时，从x移到z
    else:
        move(n - 1, x, z, y)  # n个盘时，将x的前n-1个盘借助z，移到y
        print(x, '-->', z)  # 此时y有前n-1个盘，将x上剩的最后一个盘移到z
        move(n - 1, y, x, z)  # 此时z有1个盘，将y的n-1个盘借助x，移到z


move(3, 'A', 'B', 'C')
