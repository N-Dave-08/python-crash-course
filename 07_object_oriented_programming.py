class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof")


my_dog = Dog("rex")
my_dog.bark()

another_dog = Dog("charlie")
another_dog.bark()


# Inheritance
class Dog:
    def bark(self):
        print("woof!")


class RobotDog(Dog):
    def dance(self):
        print("eyy i am dancing")


RobotDog = RobotDog()
RobotDog.dance()


# 1 and 2
class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def info(self):
        print(f"{self.make}, {self.year}")


car = Car("ford", 1970)
car.info()


# 3
class ElectricalCar(Car):
    def __init__(self, make, year, battery_size):
        super().__init__(make, year)
        self.battery_size = battery_size


ElectricalCar = ElectricalCar("dodge", 1969, 10000)
ElectricalCar.info()
