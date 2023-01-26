class Person:
    name:str
    age:int
    __spy_name:str
    def __init__(self,name:str,age:int,spy_name:str):
        self.name = name
        self.age = age
        self.__spy_name = spy_name

    def get_spy_name(self):
        return self.__spy_name
    def set_spy_name(self,spy_name:str):
        self.__spy_name = spy_name

    def __shoutout_spy_name(self):    #private function because it has __ in the begining
        print(self.__spy_name.upper())

    def public_shoutout(self):
        self.__shoutout_spy_name()

    def test_spy_name(self):
        print(self.__spy_name.lower())

    #static method
    @staticmethod
    def say_hi(name:str):
        print("Hi " + name)

anton = Person("Anton",30,"Beardboy")

#anton.name = "Evert"
#anton.__spy_name = "Weirdboy"

print(anton.name)
#print(anton.__spy_name)
anton.set_spy_name("HejBoy")
print(anton.get_spy_name())
anton.public_shoutout()
anton.test_spy_name()

anton.say_hi("My friend")


class Calculator:
    @staticmethod
    def add(a,b):
        return  a + b
    
    @staticmethod
    def substract(a,b):
        return  a - b

    @staticmethod
    def multiply(a,b):
        return  a * b

    @staticmethod
    def devide(a, b):
        return a / b
res = Calculator.add(1,2)
print(res)

res = Calculator.substract(1, 2)
print(res)

res = Calculator.multiply(1, 2)
print(res)

res = Calculator.devide(1, 2)
print(res)

my_calc = Calculator()
res = my_calc.add(10,15)
print(res)
