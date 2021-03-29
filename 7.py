a=100
while a<1000:
    b=str(a)
    c=b[0]
    d=b[1]
    e=b[2]
    f=int(c)
    g=int(d)
    h=int(e)
    if a==f**3+g**3+h**3:
        print(a,end=",")
        a+=1
    else:
        a+=1