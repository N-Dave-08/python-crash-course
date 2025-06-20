# Module 3: Functions and Scope

## Overview
Functions help organize code into reusable blocks. Scope determines where variables are accessible.

---

## Defining Functions
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

### Return Values
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

---

## Parameters and Arguments
- **Positional arguments:** Order matters
- **Keyword arguments:** Specify by name
- **Default values:**
```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(3, 3))   # 27
```

---

## Variable Scope
- **Local:** Inside a function
- **Global:** Outside all functions

```python
x = 10  # global

def foo():
    x = 5  # local
    print(x)

foo()      # 5
print(x)   # 10
```

---

## Mini Exercises
1. Write a function that returns the square of a number.
2. Write a function that greets a user by name.
3. What will this print?
```python
def test():
    y = 7
    print(y)
test()
print(y)
```

### Answers
```python
# 1
def square(n):
    return n * n

# 2
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")

# 3
# It will print 7, then raise a NameError because y is not defined outside the function.
```

---

## Real-World Use Case
Suppose you want to calculate the total price with tax:
```python
def total_with_tax(price, tax_rate=0.08):
    return price * (1 + tax_rate)

print(total_with_tax(100))  # 108.0
``` 