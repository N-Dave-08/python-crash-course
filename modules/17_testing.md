# Module 17: Testing with unittest and pytest

## Overview
Testing ensures your code works as expected. Python has built-in `unittest` and third-party `pytest` frameworks.

---

## unittest Example
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# Run with: python -m unittest filename.py
```

---

## pytest Example
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

# Run with: pytest filename.py
```

---

## Mini Exercises
1. Write a unittest for a function that multiplies two numbers.
2. Write a pytest for a function that checks if a string is a palindrome.

### Answers
```python
# 1
import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

# 2
def is_palindrome(s):
    return s == s[::-1]

def test_is_palindrome():
    assert is_palindrome("level")
```

---

## Real-World Use Case
Suppose you want to test a function that fetches data from an API. You can use `unittest.mock` to mock the API response.
```python
from unittest.mock import patch
import requests

def get_data(url):
    return requests.get(url).json()

@patch('requests.get')
def test_get_data(mock_get):
    mock_get.return_value.json.return_value = {"x": 1}
    assert get_data("fakeurl") == {"x": 1}
``` 