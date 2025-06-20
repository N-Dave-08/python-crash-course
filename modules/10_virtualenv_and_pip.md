# Module 10: Virtual Environments and pip

## Overview
Virtual environments let you manage dependencies for different projects. `pip` is Python's package installer.

---

## Creating a Virtual Environment
```sh
python -m venv venv
```
Activate it:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

---

## Installing Packages with pip
```sh
pip install requests
```

## Listing and Freezing Packages
```sh
pip list
pip freeze > requirements.txt
```

---

## Mini Exercises
1. Create a virtual environment and activate it.
2. Install the `requests` package.
3. Save installed packages to `requirements.txt`.

### Answers
```sh
# 1
python -m venv venv
# Activate as above

# 2
pip install requests

# 3
pip freeze > requirements.txt
```

---

## Real-World Use Case
Suppose you want to share your project:
- Create a `requirements.txt` with `pip freeze > requirements.txt`
- Others can install dependencies with `pip install -r requirements.txt` 