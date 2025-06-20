# Module 13: Web Scraping (requests & BeautifulSoup)

## Overview
Web scraping is extracting data from websites. Python's `requests` and `BeautifulSoup` libraries make this easy.

---

## Installing Required Libraries
```sh
pip install requests beautifulsoup4
```

---

## Fetching a Web Page
```python
import requests
response = requests.get("https://example.com")
print(response.text)
```

---

## Parsing HTML with BeautifulSoup
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)
```

---

## Mini Exercises
1. Fetch the HTML of `https://example.com` and print the first 100 characters.
2. Use BeautifulSoup to extract all the links (`<a>` tags) from a page.

### Answers
```python
# 1
import requests
r = requests.get("https://example.com")
print(r.text[:100])

# 2
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
for link in soup.find_all("a"):
    print(link.get("href"))
```

---

## Real-World Use Case
Suppose you want to get all headlines from a news site:
```python
import requests
from bs4 import BeautifulSoup
url = "https://news.ycombinator.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
for title in soup.find_all("a", class_="storylink"):
    print(title.text)
``` 