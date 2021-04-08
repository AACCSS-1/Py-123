from math import sqrt
def s(num):
	x=sqrt(num)
	y=num/2
	count=1
	while abs(y-x)>10**(-6):
		count+=1
		y=((y*1.0)+(1.0*num)/y)/2
	return y
 
x=eval(input())
print(s(x))