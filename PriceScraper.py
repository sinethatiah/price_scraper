import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


try:
    API_KEY = "48cb79b886cfdf2c5b39e959"
    exchange_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/GBP/KES"
    exchange_response = requests.get(exchange_url)
    exchange_response.raise_for_status()
    rate = exchange_response.json()["conversion_rate"]
    print(f"Exchange rate fetched: 1 GBP = {rate} KES")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to exchange rate API.")
except requests.exceptions.HTTPError as e:
    print(f"Error: Exchange rate API returned bad response — {e}")


try:
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    print(f"Found {len(books)} books.")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to books website.")
except requests.exceptions.HTTPError as e:
    print(f"Error: Books site returned bad response — {e}")



try:
    book_data = []
    for book in books:
        book_title = book.h3.a["title"]
        raw_price = book.find("p", class_="price_color").text
        price_gbp = float(raw_price.replace("£", "").replace("Â£", "").strip())
        price_kes = round(price_gbp * rate, 2)
        book_data.append([book_title, price_gbp, price_kes])

    df = pd.DataFrame(book_data, columns=["Title", "Price (GBP)", "Price (KES)"])
    
    
    print(df.to_string(index=False))

    print("Saving CSV...")
    df.to_csv(r"C:\Users\ADMIN\desktop\javascript\price_scraper\books.csv", index=False)
    print("\nDone! books.csv created.")

except Exception as e:
    print(f"Error processing data: {e}")
