import requests

if __name__ == '__main__':
    kw = {"wd": "长城"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}
    response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
    # print(response.text)
    # print(response.content.decode("utf-8"))
    print(response.status_code)
