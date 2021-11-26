import random
shop = [
    ["酱油", 20],
    ["醋", 15],
    ["腊肠", 50],
    ["卫龙", 5.5],
    ["电饭煲", 299],
    ["威猛先生", 60],
    ["软华子", 70],
    ["鸡蛋面", 10]
]
mycar = []
money = 1000
print('恭喜您,今天搞活动,所有商品一律八折,还能抽取折上折和免单！')
while True:
    a = input("请输入，10086，抽取您的优惠券:")
    if a == "10086":
        w = random.randint(1, 31)
        if w <= 10:
            print("恭喜您,抽中了卫龙三折优惠卷")
            b = 0.3
            break
        elif 10 < w <= 30:
            print("恭喜您,抽中了威猛先生九折优惠卷")
            b = 0.9
            break
        else:
            print("恭喜您，抽中免单券")
            b = 0
            break
    else:
        print("输入错误,请重新输入‘10086’进行抽取优惠卷.")
while True:
    for i in enumerate(shop):
        print(i)
    n = input("请选择商品")
    if n.isdigit():
        n = int(n)
        if n < len(shop):
            if money > shop[n][1]:
                mycar.append(shop[n])
                if n == 3 and b == 0.3:
                    money = money - shop[n][1] * b * 0.8
                elif n == 4 and b == 0.9:
                    money = money - shop[n][1] * b * 0.8
                elif b == 0:
                    money = money
                else:
                    money = money - shop[n][1] * 0.8
                    print("此商品已经加入购物车，您的余额为：", money)
            else:
                print("余额不足,您的余额为：", money)
        else:
            print("请输入正确的商品编号")
    elif n == "q" or n == "Q":
        print("再见,以下是您购买的商品,您的余额剩余：",money)
        for i in enumerate(mycar):
            print(i)
        break
    else:
        print("您输入的有误")