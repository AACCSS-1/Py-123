a=[60,59,66,90,98,18,48,65,87,25,96,94,52,87,69,78,24,98]
print(a)
no=[]
great=[]
for i in a:
    if i<60:
        no.append(i)
    if i>=90:
        great.append(i)
print(no,great)
avegno=sum(no)/len(no)
aveggreat=sum(great)/len(great)
print("不及格平均分：{:.2f}，优秀平均分：{:.2f}".format(avegno,aveggreat))