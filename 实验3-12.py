
import random as r
x=0
while x==0:
    a=r.randint(1,10)
    b=r.randint(1,10)
    print("{} + {} = ?".format(a,b))
    c=a+b
    d=input("请输入两个数的和，退出请输入quit:")
    if d=="quit":
        x=1
    else:
        d=eval(d)
        if d==c:
            print("计算正确！")
        else:
            print("{} + {}应该等于 {} ，您的运算错误，继续努力!".format(a,b,c))
