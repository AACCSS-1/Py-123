for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                e=1000*a+100*b+10*c+d
                f=100*c+10*d+c
                g=100*a+10*b+c
                if e-f==g:
                    print("A={},B={},C={},D={}".format(a,b,c,d))