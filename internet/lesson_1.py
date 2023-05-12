import requests, bs4

url = 'https://market.yandex.ru/catalog--mobilnye-telefony/54726/list?hid=91491&onstock=1&local-offers-first=0'
r = requests.get(url)
r.encoding = 'UTF8'
print(r.text)
b = bs4.BeautifulSoup(r.text, "html.parser")

atitles = b.select("div.n-snippet-cell2__title a")

titles = []

for a in atitles:
    titles.append(a.getText())

print(titles)