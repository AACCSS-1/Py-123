#编写程序，求2！+4！+6！+8！+10！
import math
x=2
s=0
while x<=10:
    s=s+math.factorial(x)
    x=x+2
print(s)