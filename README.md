# Price Scraper

Scrapes book titles and prices from [books.toscrape.com](https://books.toscrape.com/), converts prices from GBP to KES using live exchange rates, and saves the results to a CSV file.

## Features

- Scrapes book titles and prices
- Converts GBP → KES via [ExchangeRate-API](https://www.exchangerate-api.com/)
- Displays results in a clean table (pandas)
- Saves output to `books.csv`
- Handles connection and HTTP errors 

## Requirements

```bash
pip install -r requirements.txt
```

## Setup

1. Get a free API key from [ExchangeRate-API](https://www.exchangerate-api.com/)
2. Replace the `API_KEY` value in `PriceScraper.py` with your own key

## Usage

```bash
python PriceScraper.py
```

Output is printed to the terminal and saved as `books.csv` in the project folder.