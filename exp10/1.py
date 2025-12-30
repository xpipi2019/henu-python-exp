"""
使用Request和Bs4模块爬取豆瓣电影TOP250排行榜的电影名称、链接、评分信息等信，并将数据保存在films.csv中。
网站：https://movie.douban.com/top250
"""

import csv

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

films = []

for start in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={start}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("div", class_="item")
    for item in items:
        hd = item.find("div", class_="hd")
        if hd:
            a_tag = hd.find("a")
            if a_tag:
                title_span = a_tag.find("span", class_="title")
                name = title_span.text if title_span else ""
                link = a_tag.get("href", "")
            else:
                name = ""
                link = ""
        else:
            name = ""
            link = ""

        rating_span = item.find("span", class_="rating_num")
        rating = rating_span.text.strip() if rating_span else ""

        films.append([name, link, rating])

with open("films.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["电影名称", "链接", "评分"])
    writer.writerows(films)
