a,b,c=eval(input())
det=b**2-4*a*c
if a==0:
    x=-c/b
else:
    x1=(-b-det**(1/2))/2
    x2=(-b+det**(1/2))/2
    if det==0:
        print(x1)
    if det>0:
        print(x1,x2)
    if det<0:
        print(x1,x2)
