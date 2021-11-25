import random
our=random.randint(0,50)
print(our)
gold=5000
frequency=0
lock=0
i=1
while  True:
    nuw=input("请输入你要猜的数字")
    nuw=int(nuw)
    if nuw==our:
        frequency+=1
        gold+=300
        print('恭喜您猜中了，当前剩余金币',gold,"已经猜的次数",frequency)
        i=i+1
    elif nuw>our:
        gold-=100
        frequency+=1
        print("大了,当前剩余金币,",gold,"已经猜的次数:",frequency)
    if gold==lock:
        print("金币不足，锁定")
        i=i+1
    elif nuw<our:
        gold-=1000
        frequency+=1
        print("小了，您的金币还剩",gold,"已经猜的次数:",frequency)
        if gold==lock:
            print("金币不足，锁定")
        i=i+1
