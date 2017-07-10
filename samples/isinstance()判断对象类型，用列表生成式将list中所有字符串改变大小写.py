L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)  # 期待输出: ['hello', 'world', 'apple']

L3 = [(s.upper() if isinstance(s, str) else s) for s in L1]
print(L3)  # 期待输出: ['HELLO', 'WORLD', 18, 'APPLE', None]
