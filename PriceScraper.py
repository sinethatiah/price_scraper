import requests
from bs4 import  BeautifulSoup
import csv

url="https://books.toscrape.com/"
response= requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")

Book_data=[]
books=soup.find_all("article" , class_="product_pod")

for book in books:
    book_title=book.h3.a["title"]
    book_price=book.find("p", class_="price_color").text
    print(f"{book_price},{book_title}")
