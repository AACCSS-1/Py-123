a=input()
#判断数字个数
int_c=0
for i in (a):
    if i.isdigit()==True:
        int_c+=1
digit=int_c
#判断中英文字母个数
let_c=0
for i in (a):
    if i.isalpha()==True:
        let_c+=1
letter=let_c
#判断其他字符数量
b=len(a)
other=b-digit-letter
print("letter = {}, digit = {}, other = {}".format(letter, digit, other))