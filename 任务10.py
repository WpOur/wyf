class Oldcook:
    __name = ""
    __age = 0

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        if age < 0 or age > 120:
            print("年龄非法！")
        else:
            self.__age = age

    def getAge(self):
        return self.__age

    def steamrice(self):
        print("厨师",self.__name,"正在蒸饭")


class Youngcook(Oldcook):

    def stirfry(self):
        print("厨师",self.getName(),"正在炒菜")

class Littlecook(Youngcook,Oldcook):

    def cooking(self):
        print("厨师", self.getName(), "正在炒菜")

cook = Littlecook()
cook.setName("小阿飞")
cook.setAge(12)
cook.cooking()