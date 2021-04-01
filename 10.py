for i in range(1,1000):
    n=0
    for m in range(1,i):
        if i%m==0:
            n+=m
            if i==n:
                print(i)
        
