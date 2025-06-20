# Module 11: Decorators and Generators

## Overview
Decorators modify the behavior of functions. Generators produce values lazily, saving memory.

---

## Decorators
```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()
```

---

## Generators
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)
```

---

## Mini Exercises
1. Write a decorator that prints "Start" before a function runs.
2. Write a generator that yields even numbers up to 10.

### Answers
```python
# 1
def start_decorator(func):
    def wrapper():
        print("Start")
        func()
    return wrapper

# 2
def even_gen():
    for i in range(0, 11, 2):
        yield i
```

---

## Real-World Use Case
Suppose you want to log function calls:
```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    return a + b

add(2, 3)
``` 