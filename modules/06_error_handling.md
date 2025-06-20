# Module 6: Error Handling and Exceptions

## Overview
Error handling lets you manage unexpected situations and keep your programs running smoothly.

---

## try/except
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## else and finally
```python
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")
finally:
    print("This runs no matter what.")
```

## Raising Exceptions
```python
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero!")
    return a / b
```

---

## Mini Exercises
1. Write code that catches a ValueError when converting input to int.
2. Write a function that raises an exception if a number is negative.

### Answers
```python
# 1
try:
    num = int("abc")
except ValueError:
    print("Not a number!")

# 2
def check_positive(n):
    if n < 0:
        raise ValueError("Negative!")
```

---

## Real-World Use Case
Suppose you want to ensure user input is valid:
```python
def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Please enter a valid number.")
``` 