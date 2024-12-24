import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import random
import pandas as pd
import json


def send_request(ur):
    ua = UserAgent()
    header = {"User-Agent": ua.random,
              "Language": "en-US;q=0.9",
              "Encoding": "gzip, deflate, br",
              "Connection": "keep-alive",
              "DNT": "1"}
    res = requests.get(ur, headers=header)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


def scrape_all_coins(soup):
    lst = []
    print("Scraping process is going to start. Hold On")
    rows = soup.find_all("tr")
    for row in rows[1:]:
        table_datas = row.find_all('td')
        if len(table_datas) <= 2:
            print("No sufficient data in this row.")
            continue

        td = table_datas[2]
        currency = td.find('a')
        if not currency:
            print("Currency doesn't exist in this row.")
            continue

        # Get the currency link
        currency_link = currency.get("href", "")
        if not currency_link.startswith("https"):
            currency_link = "https://www.coinmarketcap.com" + currency_link

        try:
            # Extract currency name and nickname
            currency_name = None
            currency_nick_name = None

            currency_name_ach = currency.find('div', class_="sc-65e7f566-0 sc-e8147118-0 eQBACe dxqfPq")
            if currency_name_ach:
                hahaha = currency_name_ach.find('div', class_="sc-65e7f566-0 sc-e8147118-1 eQBACe jtrNaf")
                if hahaha:
                    hehehe = hahaha.find("div")
                    if hehehe:
                        currency_name = hehehe.find("p", class_="sc-65e7f566-0 iPbTJf coin-item-name")
                        currency_nick_name = hahaha.find("div", class_="sc-e8147118-3 jcakMR").find("p", class_="sc-65e7f566-0 byYAWx coin-item-symbol")
                        if currency_name:
                            currency_name = currency_name.text
                        if currency_nick_name:
                            currency_nick_name = currency_nick_name.text
                else:
                    print("Error: 'hahaha' block not found.")
            else:
                print("")
            price = table_datas[3].text
            # If no names were found, attempt fallback parsing
            if not currency_name or not currency_nick_name or not price:
                spans = td.find("a").find_all("span")
                for i in spans[1]:
                    currency_name = i.text
                currency_nick_name = td.find('a').find("span", {'class': 'crypto-symbol'}).text
                price = table_datas[3].text
            # print(f"Name: {currency_name}, Short Name: {currency_nick_name}, price: {price}, Link: {currency_link}")
            lst.append({"Crypto Name": currency_name,
                        "Crypto Symbol": currency_nick_name,
                        "Current Price": price,
                        "More Details": currency_link})

        except Exception as e:
            print(f"Error while parsing data: {e}")
    return lst


if __name__ == "__main__":
    lst_to_store = []
    for i in range(1, 106):
        print(f"Scraping page {i}.")
        url = f"https://coinmarketcap.com/?page={i}"
        time.sleep(random.uniform(2, 5))
        s = send_request(ur=url)
        lst = scrape_all_coins(soup=s)
        lst_to_store.extend(lst)

    df = pd.DataFrame(lst_to_store)
    df.to_csv("crypto_trends.csv", index=False)
    df.to_excel("crypto_trends.xlsx", index=False)
    with open("crypto_trends.json", "w", encoding="utf-8") as file:
        json.dump(lst_to_store, file, ensure_ascii=False, indent=2)
    print("Data stored to csv, excel and json.")
