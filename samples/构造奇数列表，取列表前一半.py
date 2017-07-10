# 构造奇数list L: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
L = []
for n in range(1, 20, 2):
    L.append(n)
print('L:', L)

# 取list的前一半的元素 H: [1, 3, 5, 7, 9]
H = []
for i in range(0, int(len(L) / 2)):
    H.append(L[i])
print('H:', H)
