# Classes are blueprints for objects. They can contain methods and variables.
# Objects are instances of classes. They can access methods and variables of the class.

# method,variables,instance variables,constructor,inheritance,encapsulation,abstraction,polymorphism
# Self Keyword is mandatory for calling variable names into method
# Instance and class variables have whole different purpose
# Constructor name should be __init__

class Calculator:
    num = 100  # class variables

    # default constructor

    def __init__(self):  # Constructor
        print("Inside constructor")

    def getdata(self):
        print("Inside getData of Calculator")

    def sum(self, a, b):
        return a + b + Calculator.num


obj = Calculator()  # Object creation
obj.getdata()  # Method calling
print(obj.num)  # Variable calling

obj1 = Calculator()
print(obj1.sum(4, 5))
