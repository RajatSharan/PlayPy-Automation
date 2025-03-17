from python_Basics.oopsBasics import Calculator


class Childin(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self)
        print("Inside Childin Constructor")


    def getCompletedata(self):
        print("Inside getData of Childin")
        return self.num + self.num2


obj3=Childin()
print(obj3.getCompletedata())

