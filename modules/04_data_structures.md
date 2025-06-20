# Module 4: Data Structures (Lists, Tuples, Sets, Dictionaries)

## Overview
Data structures help organize and store data efficiently. Python's built-in data structures are powerful and flexible.

---

## Lists
Ordered, mutable collections.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
fruits.append("orange")
print(fruits)
```

---

## Tuples
Ordered, immutable collections.
```python
point = (3, 4)
print(point[1])  # 4
```

---

## Sets
Unordered, unique elements.
```python
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)
```

---

## Dictionaries
Key-value pairs.
```python
person = {"name": "Alice", "age": 30}
print(person["name"])
person["city"] = "New York"
print(person)
```

---

## Mini Exercises
1. Create a list of your three favorite movies and print the second one.
2. Make a tuple with your birth year and month.
3. Add a new color to a set.
4. Create a dictionary for a book with keys: title, author, year.

### Answers
```python
# 1
movies = ["Inception", "Matrix", "Interstellar"]
print(movies[1])

# 2
birth = (1990, 5)

# 3
colors = {"red", "blue"}
colors.add("green")

# 4
book = {"title": "1984", "author": "Orwell", "year": 1949}
```

---

## Real-World Use Case
Suppose you want to count word frequencies in a sentence:
```python
sentence = "hello world hello"
words = sentence.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)  # {'hello': 2, 'world': 1}
``` 