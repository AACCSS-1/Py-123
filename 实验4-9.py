username=input("注册：请输入账号：")
passport=input("注册：请输入密码：")
a={username:passport}
for i in range(3):
    b=input("请输入账号：")
    c=input("请输入密码：")
    if c==a.get(b):
        print("Welcome!")
        break
else:
    print("无法登陆")