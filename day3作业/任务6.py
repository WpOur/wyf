name = "root"
password = "admin"
for i in range(0,5):
    username=input("请输入用户名:")
    userps=input("请输入用户密码:")
    if username==name and userps==password:
        print("登录成功")
    elif name!=username or password!=userps:
        if i <=3:
            print("用户名或密码错误")
        else:
            print("对不起，您的账户已锁定")