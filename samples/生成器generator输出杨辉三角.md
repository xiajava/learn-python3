[杨辉三角](http://baike.baidu.com/view/7804.htm)定义如下：

![](https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike72%2C5%2C5%2C72%2C24/sign=1fadd0bb32d12f2eda08a6322eabbe07/d833c895d143ad4bb552f7ac86025aafa40f0659.jpg)

自己想的方法用了两个list，Ln头尾手动添加1，中间用于接收上行L算来的数据:
```
def triangles():
    L = [1]
    while True:
        yield L

        Ln = [1]
        for i in range(1, int(len(L))):
            Ln.append(L[i - 1] + L[i])
        Ln.append(1)
        L = Ln


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
```
而这个L.append(0)在原L后添个0，利用其性质使头尾也符合计算公式，简化了代码:
```
L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]
```
