import requests
from bs4 import BeautifulSoup
import csv

API_KEY = "48cb79b886cfdf2c5b39e959"
exchange_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/GBP/KES"
exchange_response = requests.get(exchange_url)
rate = exchange_response.json()["conversion_rate"]

url = "https://books.toscrape.com/"
response = requests.get(url)
response.encoding = "utf-8"  # fix encoding here
soup = BeautifulSoup(response.text, "html.parser")

book_data = []
books = soup.find_all("article", class_="product_pod")

for book in books:
    book_title = book.h3.a["title"]
    raw_price = book.find("p", class_="price_color").text
    price_gbp = float(raw_price.replace("£", "").replace("Â£", "").strip())
    price_kes = round(price_gbp * rate, 2)
    print(f"{book_title} | £{price_gbp} | KES {price_kes}")



