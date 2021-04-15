score={'Han':65,'Wang':97,'Ma':73,'Xu':85,'Yang':92}
s={65:'Han',97:'Wang',73:'Ma',85:'Xu',92:'Yang'}
score1=score.copy()
b=list(score1.items())
c=[]
for i in range(5):
    c.append(b[i][1])
c.sort(reverse=True)
for i in range(5):
    print(s[c[i]])