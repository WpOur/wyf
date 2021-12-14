import time
class OldPhone:
    __phone_number = ""

    def setPhone_number(self, phone_number):
        self.__phone_number = phone_number
    def getPhone_number(self):
        return self.__phone_number

    def call(self, number):
        print(self.__phone_number, "正在给", number, "打电话")

        for i in range(8):
            print(".",end="")
            time.sleep(1)
        print("对方已接通！")

class NewPhone(OldPhone):
    __brand = ""

    def setBrand(self, brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def call(self, number):
        super().call(number)
        print("品牌为:", self.__brand, "的手机很好用")


phone = NewPhone()
phone.setPhone_number("18832058590")
phone.setBrand("摩托罗拉")
phone.call("15533069852")