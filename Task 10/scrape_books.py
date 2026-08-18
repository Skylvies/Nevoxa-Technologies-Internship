"""
Task 10: Web Scraping and Data Collection Using Python
Novexa Technologies (NVT) - Data Analysis Internship

Target site : https://books.toscrape.com/
             (an open sandbox site built specifically for scraping practice —
              see https://toscrape.com/ — so this fully complies with the
              site's Terms of Service and robots.txt, which explicitly
              allow scraping.)

What this script does
----------------------
1. Sends an HTTP GET request to each paginated catalogue page.
2. Parses the returned HTML with BeautifulSoup.
3. Extracts, for every book: Title, Price, Star Rating, Availability
   (in stock / out of stock), Number of copies in stock, UPC, Category,
   Product page URL and Cover image URL.
3. Cleans/normalises the scraped fields (strips currency symbols,
   converts word-ratings like "Three" -> 3, converts availability text
   into a boolean + numeric stock count).
4. Stores everything in a pandas DataFrame and writes it to CSV.

Usage
-----
    python scrape_books.py                 # scrapes all 50 pages (1000 books)
    python scrape_books.py --pages 5        # scrapes only the first 5 pages
    python scrape_books.py --out data/books_dataset.csv

Requirements: requests, beautifulsoup4, pandas  (pip install -r requirements.txt)
"""

import argparse
import re
import time
import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/"
CATALOGUE_URL = BASE_URL + "catalogue/page-{}.html"

# The site encodes the star rating as a CSS class name instead of plain text,
# e.g. <p class="star-rating Three">. This map converts that word to an int.
RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 NVT-Task10-Scraper/1.0"
    )
}


def get_soup(url: str, session: requests.Session) -> BeautifulSoup:
    """Fetch a URL and return a parsed BeautifulSoup object."""
    response = session.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def parse_listing_page(soup: BeautifulSoup, page_url: str) -> list[str]:
    """From a catalogue listing page, return the list of absolute product URLs."""
    product_urls = []
    for article in soup.find_all("article", class_="product_pod"):
        relative_link = article.h3.a["href"]
        product_urls.append(urljoin(page_url, relative_link))
    return product_urls


def parse_book_page(soup: BeautifulSoup, url: str) -> dict:
    """Extract all fields for a single book's product page."""
    title = soup.find("div", class_="product_main").h1.get_text(strip=True)

    price_text = soup.find("p", class_="price_color").get_text(strip=True)
    price = float(re.sub(r"[^\d.]", "", price_text))

    rating_class = soup.find("p", class_="star-rating")["class"][1]
    rating = RATING_WORDS.get(rating_class, None)

    availability_text = soup.find("p", class_="instock availability").get_text(strip=True)
    in_stock = "In stock" in availability_text
    stock_match = re.search(r"\((\d+) available\)", availability_text)
    stock_count = int(stock_match.group(1)) if stock_match else 0

    # Category = breadcrumb second-to-last item
    breadcrumb = soup.find("ul", class_="breadcrumb").find_all("li")
    category = breadcrumb[2].get_text(strip=True) if len(breadcrumb) > 2 else None

    image_rel = soup.find("div", class_="item active").img["src"]
    image_url = urljoin(url, image_rel)

    # UPC from the product information table
    upc = None
    table = soup.find("table", class_="table-striped")
    if table:
        row = table.find("th", string="UPC")
        if row:
            upc = row.find_next_sibling("td").get_text(strip=True)

    return {
        "Title": title,
        "Price (£)": price,
        "Rating (out of 5)": rating,
        "In Stock": in_stock,
        "Stock Count": stock_count,
        "Category": category,
        "UPC": upc,
        "Product URL": url,
        "Image URL": image_url,
    }


def scrape(num_pages: int) -> pd.DataFrame:
    session = requests.Session()
    records = []

    for page_num in range(1, num_pages + 1):
        page_url = CATALOGUE_URL.format(page_num)
        try:
            listing_soup = get_soup(page_url, session)
        except requests.exceptions.HTTPError:
            print(f"Page {page_num} not found — stopping (reached the last page).")
            break

        product_urls = parse_listing_page(listing_soup, page_url)
        print(f"Page {page_num}/{num_pages}: found {len(product_urls)} books")

        for product_url in product_urls:
            book_soup = get_soup(product_url, session)
            records.append(parse_book_page(book_soup, product_url))
            time.sleep(0.2)  # polite delay so we don't hammer the server

    return pd.DataFrame(records)


def main():
    parser = argparse.ArgumentParser(description="Scrape books.toscrape.com into a CSV dataset.")
    parser.add_argument("--pages", type=int, default=50, help="Number of catalogue pages to scrape (each has 20 books). Default: 50 (all 1000 books).")
    parser.add_argument("--out", type=str, default="data/books_dataset.csv", help="Output CSV path.")
    args = parser.parse_args()

    print(f"Starting scrape of {args.pages} page(s) from {BASE_URL} ...")
    df = scrape(args.pages)

    if df.empty:
        print("No data collected — check your internet connection.", file=sys.stderr)
        sys.exit(1)

    df.drop_duplicates(subset="Product URL", inplace=True)
    df.to_csv(args.out, index=False)
    print(f"\nDone. Collected {len(df)} books -> saved to {args.out}")
    print(df.head())


if __name__ == "__main__":
    main()
