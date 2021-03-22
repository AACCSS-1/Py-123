a,b=eval(input())
if b<1 or b>12 or a<0:
    print("年份或者月份不合法！")
else:
    if b==2:
        if (a%4==0 and a%100!=0) or a%400==0:
            print("{}年{}月有{}天".format(a,b,29))
        else:
            print("{}年{}月有{}天".format(a,b,28))
    else:
        if b<=7:
            c=b%2
            if c==1:
                print("{}年{}月有{}天".format(a,b,31))
            else:
                print("{}年{}月有{}天".format(a,b,30))
        if b>=7:
            c=b%2
            if c==1:
                print("{}年{}月有{}天".format(a,b,30))
            else:
                print("{}年{}月有{}天".format(a,b,31))