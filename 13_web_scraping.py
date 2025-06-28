import requests
import json
from bs4 import BeautifulSoup




# use case
url = "https://news.ycombinator.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

selectors = [
    "a.titleline",
    "a.storylink", 
    "span.titleline a",
    "td.title a",
    "a[href*='item?id=']"
]

headlines = []
for selector in selectors:
    titles = soup.select(selector)
    if titles:
        print(f"Found {len(titles)} headlines with selector: {selector}")
        headlines = [title.text.strip() for title in titles if title.text.strip()]
        break

if headlines:
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for headline in headlines:
            file.write(headline + "\n")
            print(headline)
    print(f"Saved {len(headlines)} headlines to headlines.txt")
else:
    print("No headlines found with any selector")
