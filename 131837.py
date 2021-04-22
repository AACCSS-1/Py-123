def f(a):
    for i in range(2,a):
        if a%i==0:
            break
    else:
        return a

a=eval(input())
b=eval(input())
s=0
for i in range(a,b+1):
    if f(i)==i:
        s=s+i**2
print(s)