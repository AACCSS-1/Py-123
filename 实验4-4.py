a=[]
for i in range(10):
    a.append(eval(input()))
a.sort()
print(a)
a.pop(0)
a.pop(-1)
print(a)
aver=sum(a)/len(a)
print("{:.2f}".format(aver))