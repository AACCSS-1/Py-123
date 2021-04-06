def qwe(a):
    if a==1:
        return 1
    if a==2:
        return 2
    if a==3:
        return 3
    else:
        x=qwe(a-1)+qwe(a-2)+qwe(a-3)
        return x
for i in range(4,100):
    if qwe(i)>2000:
        print(i)
        break