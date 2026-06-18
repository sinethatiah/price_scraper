import requests
from bs4 import  BeautifulSoup
import csv

API_KEY="48cb79b886cfdf2c5b39e959"
exchange_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/GBP/KES"
exchange_response=requests.get(exchange_url)
rate = exchange_response.json()["conversion_rate"]


url="https://books.toscrape.com/"
response= requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")

Book_data=[]
books=soup.find_all("article" , class_="product_pod")

for book in books:
    book_title=book.h3.a["title"]
    book_price=book.find("p", class_="price_color").text
    print(f"{book_price},{book_title}")



