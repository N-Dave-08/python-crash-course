# Module 8: Modules and Packages

## Overview
Modules and packages help organize code into reusable files and directories.

---

## Importing Modules
```python
import math
print(math.sqrt(16))  # 4.0
```

## Creating Your Own Module
Create a file `mymodule.py`:
```python
def greet(name):
    print(f"Hello, {name}!")
```
Use it in another file:
```python
import mymodule
mymodule.greet("Alice")
```

---

## Packages
A package is a directory with an `__init__.py` file.

---

## Mini Exercises
1. Import the `random` module and print a random number.
2. Create a module with a function that returns the square of a number.

### Answers
```python
# 1
import random
print(random.randint(1, 10))

# 2
# In square.py:
def square(n):
    return n * n
# In another file:
# import square
# print(square.square(4))
```

---

## Real-World Use Case
Suppose you want to split your project into multiple files for clarity and reuse:
```python
# In utils.py
def add(a, b):
    return a + b
# In main.py
import utils
print(utils.add(2, 3))
``` 