far = []
high = 100
for i in range(1, 11):
    if i == 1:
        far.append(high)
    else:
        far.append(high * 2)
    high = high / 2
a=sum(far)
print("经过的总距离：{:.2f}".format(a))
print("第十次反弹多高：{:.2f}".format(high))