s=0
for i in range(2,100):
  for num in range(2,i):
    if i%num==0:
      break
  else:   
    s+=i
print(s)