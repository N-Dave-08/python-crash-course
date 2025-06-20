# Module 5: File Handling

## Overview
File handling allows you to read from and write to files, enabling persistent data storage.

---

## Reading Files
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## Writing Files
```python
with open("output.txt", "w") as file:
    file.write("Hello, file!")
```

## Appending to Files
```python
with open("output.txt", "a") as file:
    file.write("\nAnother line.")
```

---

## Mini Exercises
1. Write a program that writes your name to a file called `myname.txt`.
2. Read the contents of `myname.txt` and print it.

### Answers
```python
# 1
with open("myname.txt", "w") as f:
    f.write("Alice")

# 2
with open("myname.txt", "r") as f:
    print(f.read())
```

---

## Real-World Use Case
Suppose you want to log errors to a file:
```python
def log_error(message):
    with open("error.log", "a") as f:
        f.write(message + "\n")

log_error("Something went wrong!")
``` 