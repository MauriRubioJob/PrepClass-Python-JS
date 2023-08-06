import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_html(url):
    r = requests.get(url)
    if not r.status_code == 200:
        exit("Status code:", r.status_code)
    print("GET successful.")
    return r.text


def find_price_statistics(soup):
    h2 = soup.find("h2", text="BTC Price Statistics")
    return h2.parent.div.table.tbody


def get_btc_statistics(statistics_soup):
    return statistics_soup.tr.td.text


url = "https://coinmarketcap.com/currencies/bitcoin/"
soup = BeautifulSoup(get_html(url), features="html.parser")

statistics_soup = find_price_statistics(soup)
price = "Price today: " + get_btc_statistics(statistics_soup)

with open("btc_price_history.txt", "a") as file:
    now = str(datetime.now())
    data = f"{now} {price}\n"
    file.write(data)
    print("Saved to disk.")