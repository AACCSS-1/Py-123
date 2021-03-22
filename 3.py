a=eval(input())
b=eval(input())
c=eval(input())
if a<=0 or b<=0 or c<=0:
    print("数据不合法!")
else:
    if a+b<=c or a+c<=b or b+c<=a:
        print("不能构成三角形!")
    else:
        h=(a+b+c)/2
        s=(h*(h-a)*(h-b)*(h-c))**(1/2)
        print(format(s,".2f"))
