import random
a=random.randint(100,201)
b=random.randint(100,201)
def MaxCommDivisor(m,n):
  while m * n != 0:
    m = m % n
    if m == 0:
      return n
    else:
      n = n % m
      if n == 0:
        return m
c=MaxCommDivisor(a,b)
print("{}和{}的最大公约数是{}".format(a,b,c))
def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
 
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
 
    return lcm
d=lcm(a,b)
print("{}和{}的最小公倍数是{}".format(a,b,d))