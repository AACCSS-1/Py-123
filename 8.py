for a in range(1,1001):
    b=str(a)
    c=a**2
    d=str(c)
    e=len(b)
    if e==1:
        if d[-1]==b:
            print(a)
    else:
        if d[-1:-e]==b:
            print(a)   