# Module 9: Pythonic Best Practices

## Overview
Writing Pythonic code means following conventions and using features that make code clean, readable, and efficient.

---

## Naming Conventions
- Variables: `snake_case`
- Classes: `CamelCase`
- Constants: `ALL_CAPS`

---

## List Comprehensions
```python
squares = [x * x for x in range(5)]
print(squares)
```

---

## Unpacking
```python
a, b = (1, 2)
print(a, b)
```

---

## Using `enumerate` and `zip`
```python
for idx, value in enumerate(["a", "b"]):
    print(idx, value)

for a, b in zip([1, 2], ["x", "y"]):
    print(a, b)
```

---

## Mini Exercises
1. Write a list comprehension for even numbers from 0 to 10.
2. Unpack a tuple `(5, 10)` into variables.

### Answers
```python
# 1
evens = [x for x in range(11) if x % 2 == 0]

# 2
a, b = (5, 10)
```

---

## Real-World Use Case
Suppose you want to filter a list of names:
```python
names = ["Anna", "Bob", "Alice"]
short_names = [n for n in names if len(n) <= 4]
print(short_names)  # ['Anna', 'Bob']
``` 