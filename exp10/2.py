"""
爬取TIOBE网站中的编程语言排名信息，将排名、编程语言名以及评级等信，并将数据保存在result.csv中。
网站：https://www.tiobe.com/tiobe-index/
"""

import csv

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.tiobe.com/tiobe-index/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

results = []

table = soup.find("table", id="top20")
if not table:
    table = soup.find("table")

if table:
    rows = table.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 6:
            continue

        rank = cols[0].text.strip()
        if not rank.isdigit():
            continue

        name = cols[4].text.strip() if len(cols) > 4 else ""
        rating = cols[5].text.strip() if len(cols) > 5 else ""

        if name and rank.isdigit():
            results.append([rank, name, rating])

with open("result.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["排名", "编程语言", "评级"])
    writer.writerows(results)
