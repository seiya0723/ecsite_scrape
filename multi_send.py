import requests,bs4

URL     = "http://127.0.0.1:8000/"
TIMEOUT = 10
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

client  = requests.session()
client.get(URL,timeout=TIMEOUT,headers=HEADERS)


if 'csrftoken' in client.cookies:
    csrftoken = client.cookies['csrftoken']


# Django側がgetlistで取得・保存する場合、このように文字列のリストを形成、送信する。
# 数値型、日付型なども文字列型で送信。日付はフォーマットに注意。

data                    = { "csrfmiddlewaretoken":csrftoken }

data["update_date"]     = ["2023-04-07","2023-04-07"]
data["name"]            = ["name","name"]
data["price"]           = ["3000","3000"]
data["average"]         = ["3.5","3.5"]
data["volume"]          = ["10","10"]
data["rank"]            = ["1","1"]
data["shop_code"]       = ["test","test"]
data["item_url"]        = ["http://127.0.0.1:8000/","http://127.0.0.1:8000/"]

r   = client.post(URL,data=data,headers={"Referer":URL})
print(r)
