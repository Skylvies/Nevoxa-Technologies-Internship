# NVT Task 10 — Web Scraping and Data Collection Using Python

Scrapes book data (title, price, rating, availability, stock count, category,
UPC, product URL, cover image URL) from **[books.toscrape.com](https://books.toscrape.com/)**,
an open sandbox site built specifically for scraping practice — see
[toscrape.com](https://toscrape.com/) — so this project fully complies with
the target site's Terms of Service and robots.txt.

## Repository contents

| File | Description |
|---|---|
| `scrape_books.py` | Main scraping script (requests + BeautifulSoup + pandas) |
| `scrape_books.ipynb` | Same logic as a step-by-step Jupyter notebook |
| `data/books_dataset.csv` | Collected dataset |
| `Web_Scraping_Report.md` | Report: methodology, challenges, findings |
| `requirements.txt` | Python dependencies |

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Scrape all 50 catalogue pages (~1000 books)
python scrape_books.py

# Scrape just the first N pages, custom output path
python scrape_books.py --pages 5 --out data/books_dataset.csv
```

Or open `scrape_books.ipynb` in Jupyter / VS Code and run all cells.

## How it works

1. **Request** — `requests.Session()` sends a GET request to each paginated
   catalogue page (`/catalogue/page-N.html`), then to each individual book's
   product page.
2. **Parse** — `BeautifulSoup` parses the returned HTML and locates the
   product elements (`article.product_pod`), price (`p.price_color`), star
   rating (encoded as a CSS class, e.g. `star-rating Three`), stock
   availability text, breadcrumb category, UPC table row, and cover image.
3. **Clean** — prices are stripped of the `£` symbol and cast to `float`;
   the word-rating (`"Three"`) is mapped to an integer (`3`); availability
   text is parsed into a boolean plus a numeric stock count via regex.
4. **Store** — all records are collected into a `pandas.DataFrame`,
   de-duplicated on product URL, and written to `data/books_dataset.csv`.

## Notes

- A short `time.sleep(0.2)` delay is added between requests to be polite to
  the server.
- The included `data/books_dataset.csv` is a real sample (60 books, 3
  catalogue pages) collected from the live site. Run the script with
  `--pages 50` to regenerate the complete ~1000-row dataset with every field
  (this requires a live internet connection to books.toscrape.com).
