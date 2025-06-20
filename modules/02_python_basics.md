# Module 2: Python Basics

## Overview
This module covers the foundational elements of Python: variables, data types, operators, and control flow (if, for, while). Mastering these basics is essential for all Python programming.

---

## Variables and Data Types

Variables store data. Python is dynamically typed, so you don't need to declare types explicitly.

```python
# Integer
age = 25
# Float
height = 1.75
# String
name = "Alice"
# Boolean
is_student = True
```

### Common Data Types
- int: Integer numbers
- float: Decimal numbers
- str: Text
- bool: True/False

---

## Operators

Arithmetic:
```python
x = 10
y = 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.333...
print(x // y) # 3 (floor division)
print(x % y)  # 1 (modulo)
print(x ** y) # 1000 (exponent)
```

Comparison:
```python
print(x > y)   # True
print(x == y)  # False
```

Logical:
```python
print(x > 5 and y < 5)  # True
print(not is_student)   # False
```

---

## Control Flow

### if/elif/else
```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C or below")
```

### for loop
```python
for i in range(5):
    print(i)  # 0 1 2 3 4
```

### while loop
```python
count = 0
while count < 3:
    print("Counting:", count)
    count += 1
```

---

## Mini Exercises
1. Create a variable for your favorite color and print it.
2. Write a program that checks if a number is even or odd.
3. Print numbers from 1 to 10 using a for loop.

### Answers
```python
# 1
color = "blue"
print(color)

# 2
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3
for i in range(1, 11):
    print(i)
```

---

## Real-World Use Case
Suppose you want to automate sending reminders if a task is overdue:
```python
task_due = False
if not task_due:
    print("Task is on time!")
else:
    print("Send reminder!")
``` 