def odds(a):
    alist=list(a)
    b=[]
    c=len(alist)
    for i in range(c):
        if i%2!=0:
            b.append(alist[i])
    return b

a=[1,2,3,4,5]
b=(7,8,9,10,12,13)
print(odds(a))
print(odds(b))