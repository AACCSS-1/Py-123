#编写程序,计算S=1-3+5-7+9-11……，其中项数由用户输入
a=int(input())
i=0 #控制循环次数
s=0 #求和工具人
x=1 #加数
while i<a:
    s=s+x
    x=(-1)**(i+1)*(abs(x)+2) 
    i=i+1
print(s)
