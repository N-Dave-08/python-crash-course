# Module 7: Object-Oriented Programming (OOP)

## Overview
OOP is a programming paradigm based on objects and classes. It helps organize code and model real-world entities.

---

## Classes and Objects
```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Rex")
my_dog.bark()  # Rex says woof!
```

---

## Inheritance
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow!")

cat = Cat()
cat.speak()  # Meow!
```

---

## Encapsulation and Methods
- Encapsulation: Hiding internal state
- Methods: Functions defined in a class

---

## Mini Exercises
1. Create a class `Car` with attributes `make` and `year`.
2. Add a method to print car info.
3. Create a subclass `ElectricCar` that adds a `battery_size` attribute.

### Answers
```python
# 1 & 2
class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
    def info(self):
        print(f"{self.make}, {self.year}")

# 3
class ElectricCar(Car):
    def __init__(self, make, year, battery_size):
        super().__init__(make, year)
        self.battery_size = battery_size
```

---

## Real-World Use Case
Suppose you want to model a library system:
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "Orwell")
print(book.title)
``` 