from threading import Thread
import time

eggTart = 500
cashier = 0
first_time = time.time()


class Cook(Thread):

    username = ""
    wages = 0
    count = 0

    def run(self) -> None:
        global eggTart
        global cashier
        while True:
            if time.time() - first_time < 30:
                if eggTart < 500:
                    eggTart = eggTart + 1
                    self.count = self.count + 1
                    self.wages = self.wages + 1.5
                    cashier = cashier - 1.5
                    time.sleep(0.2)
                    print("厨师", self.username, "造了一个蛋挞")
                if eggTart >= 500:
                    time.sleep(3)
            else:
                self.wages = self.count * 1.5
                print(self.username, "总共生产了", self.count, "个蛋挞,今日的工资为:", self.wages,"元")
                break


class Customer (Thread):

    username = ""
    count = 0
    money = 3000

    def run(self) -> None:
        global eggTart
        global cashier
        while True:
            if time.time() - first_time < 30:
                if eggTart > 0:
                    self.count = self.count + 1
                    self.money = self.money - 3
                    cashier = cashier + 3
                    eggTart = eggTart - 1
                    time.sleep(0.2)
                    print(self.username, "买了1个蛋挞,花了3元钱")
                if eggTart < 0:
                    time.sleep(2)
            else:
                print(self.username, "总共买了", self.count, "个蛋挞,还剩下", self.money, "元钱")
                break


p1 = Customer()
p2 = Customer()
p3 = Customer()
p4 = Customer()
p5 = Customer()
p6 = Customer()
p1.username = "顾客1"
p2.username = "顾客2"
p3.username = "顾客3"
p4.username = "顾客4"
p5.username = "顾客5"
p6.username = "顾客6"
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()

c1 = Cook()
c2 = Cook()
c3 = Cook()
c1.username = "厨师1"
c2.username = "厨师2"
c3.username = "厨师3"
c1.start()
c2.start()
c3.start()

time.sleep(35)
print("纯收益为：", cashier)