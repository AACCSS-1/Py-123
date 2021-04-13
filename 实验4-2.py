import random
a="abcdefghigklmnopqrstuvwxyz"
b=a.upper()
c="0123456789"
d=a+b+c
e=list(d)
for i in range(10):
    for h in range(8):
        print(e[random.randint(0,61)],end="")
    print()