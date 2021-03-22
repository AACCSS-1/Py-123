s=eval(input())
if s<=400:
    f=0.5*0.01*s
elif s<=600:
    f=1*0.01*s
elif s<=800:
    f=1.5*0.01*s
elif s<=1500:
    f=2*0.01*s
elif s>1500:
    f=3*0.01*s
print(format(f,".2f"))