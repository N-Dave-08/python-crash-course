# Module 16: Introduction to Web Development (Flask & FastAPI)

## Overview
Flask and FastAPI are popular frameworks for building web applications and APIs in Python.

---

## Flask: Quick Start
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

# Run with: flask run
```

---

## FastAPI: Quick Start
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

# Run with: uvicorn filename:app --reload
```

---

## Mini Exercises
1. Create a Flask route that returns "Welcome!" at `/welcome`.
2. Create a FastAPI route that returns your name at `/me`.

### Answers
```python
# 1
@app.route("/welcome")
def welcome():
    return "Welcome!"

# 2
@app.get("/me")
def me():
    return {"name": "Alice"}
```

---

## Real-World Use Case
Suppose you want to build a simple API for tasks:
```python
from fastapi import FastAPI
app = FastAPI()

tasks = []

@app.post("/tasks")
def add_task(task: str):
    tasks.append(task)
    return {"tasks": tasks}
``` 