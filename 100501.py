from math import factorial
def fac(n):
    sum=-1
    for i in range(n+1):
        sum+=factorial(i)
    return sum
n=eval(input())
print(fac(n))