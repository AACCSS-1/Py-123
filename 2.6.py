import re
x=input()
x = re.findall("\d+",x)[0]
x=eval(x)
b=x//1000
c=x-b*1000
d=c//100
e=x-1000*b-100*d
f=e//10
g=x-1000*b-100*d-10*f
print(g,f,d,b)