while True:
    h = float(input('身高/m: '))
    w = float(input('体重/kg: '))
    if h >0 and w>0:
        break
    print('输入有误')

bmi = w/h/h
if bmi < 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')
