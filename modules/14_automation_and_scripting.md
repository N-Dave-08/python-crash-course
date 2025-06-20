# Module 14: Automation and Scripting

## Overview
Python is great for automating repetitive tasks and writing scripts to save time.

---

## Automating File Operations
```python
import os
files = os.listdir(".")
for f in files:
    print(f)
```

---

## Scheduling Tasks
```python
import time
print("Start")
time.sleep(2)
print("End after 2 seconds")
```

---

## Mini Exercises
1. Write a script to rename all `.txt` files in a folder to add `_backup` to their names.
2. Write a script that prints the current time every second for 5 seconds.

### Answers
```python
# 1
import os
for filename in os.listdir("."):
    if filename.endswith(".txt"):
        os.rename(filename, filename.replace(".txt", "_backup.txt"))

# 2
import time
for _ in range(5):
    print(time.ctime())
    time.sleep(1)
```

---

## Real-World Use Case
Suppose you want to automate sending emails:
```python
import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg.set_content("Hello from Python!")
msg["Subject"] = "Test"
msg["From"] = "you@example.com"
msg["To"] = "friend@example.com"
# Uncomment and configure the next lines to actually send
# with smtplib.SMTP("smtp.example.com") as server:
#     server.login("you@example.com", "password")
#     server.send_message(msg)
``` 