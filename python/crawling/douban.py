import re
from typing import List

import requests


def parse_html(html: str) -> List[str]:
    find_film_name = r'alt="([^"]+)"'
    results = re.findall(find_film_name, html)
    return results[:-1]


def url_generator():
    base_url = "https://movie.douban.com/top250?start="
    for i in range(10):
        yield base_url + str(i * 25)


def ask_url(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/123.0.6312.59 Safari/537.36"}
    response = requests.get(url=url, headers=headers)
    # return response.content.decode("utf-8")
    return response
    # print(html)
    # res = parse_html(html)
    # print(res)


if __name__ == '__main__':
    ask_url("https://movie.douban.com/top250?start=0")
