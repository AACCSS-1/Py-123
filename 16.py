from math import factorial
def tl(a,b):
    s=a**b/factorial(b)
    return s
sum=0
x=eval(input())
i=0
while tl(x,i)>=10**(-6):
    sum+=tl(x,i)
    i+=1
print(sum)