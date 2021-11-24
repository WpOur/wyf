import random
our=random.randint(0,50)
print(our)
gold=5000
i=1
while i<=15:
    nuw=input("请输入你要猜的数字")
    nuw=int(nuw)
    if nuw==our:
        gold+=300
        print('恭喜您猜中了，当前剩余金币',gold)
        i=i+1
    elif nuw>our:
        gold-=100
        print("大了,当前剩余金币",gold)
        i=i+1
    else:
        gold-=100
        print("小了，您的金币还剩",gold)
        i=i+1


