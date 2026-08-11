# Orders Dataset — SQL for Data Analysis (Task 6)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 6**. It uses MySQL to query, filter, aggregate, and analyze a real-world orders dataset, applying core SQL techniques to answer business-relevant questions.

## 📂 Dataset
**File:** `orders.csv`
**Records:** 185,013 rows, 9 columns
**Columns:**
| Column | Description |
|---|---|
| `Customer ID` | Unique customer identifier |
| `Customer Status` | Loyalty tier — Silver / Gold / Platinum (inconsistent casing in raw data) |
| `Date Order was placed` | Order date (raw text format: DD-Mon-YY) |
| `Delivery Date` | Delivery date (raw text format: DD-Mon-YY) |
| `Order ID` | Unique order identifier (used as primary key) |
| `Product ID` | Product identifier |
| `Quantity Ordered` | Units ordered |
| `Total Retail Price for This Order` | Total price charged |
| `Cost Price Per Unit` | Cost per unit to the business |

## 🛠 Tools Used
- MySQL 8.0 (MySQL Community Server)
- MySQL command-line client / MySQL Workbench
- SQL (DDL, DML, aggregate functions, date functions)

## 🔍 Steps Performed
1. Created a dedicated database (`novexa_orders`) and `orders` table with an appropriate schema
2. Imported the dataset using `LOAD DATA LOCAL INFILE`
3. Verified row count matched the source file (185,013 rows)
4. Cleaned the data:
   - Converted raw text dates (`DD-Mon-YY`) into proper `DATE` columns using `STR_TO_DATE()`
   - Standardized inconsistent `Customer Status` casing (e.g. `Silver`/`SILVER` → `SILVER`) using `UPPER()`
   - Checked for duplicate `Order ID` values
5. Explored the dataset with `SELECT`, `WHERE`, and `ORDER BY`
6. Aggregated data using `GROUP BY` and `HAVING` to answer business questions (revenue by tier, monthly trends, top customers)
7. Wrote business insight queries covering profit margin, delivery time by tier, and best-selling products

## 📊 Key Insights

**Revenue by customer tier**
| Tier | Orders | Total Revenue | Avg Order Value |
|---|---|---|---|
| SILVER | 92,541 | $12,884,922.29 | $139.23 |
| GOLD | 88,278 | $12,172,776.44 | $137.89 |
| PLATINUM | 4,194 | $583,806.72 | $139.20 |

Despite being the premium tier, **PLATINUM customers make up only ~2.3% of orders** — SILVER and GOLD dominate order volume almost equally. Interestingly, average order value is nearly identical across all three tiers (~$137–139), meaning higher-tier customers aren't spending more per order — the tier system doesn't appear to translate into bigger basket sizes in this dataset.

**Top customers**: The single highest-spending customer (ID 7766) placed 12 orders totaling $6,826.30, but several customers hit similarly high totals with far fewer orders — e.g. customer 54290 spent $6,382.00 in a single order, showing that total spend here is influenced as much by order size as order frequency.

**Most frequent customers**: Only 14 customers placed more than 20 orders total, topping out at 26 orders (customer 91178) — repeat-purchase behavior is fairly limited across the customer base.

**Delivery time**: Average delivery time is effectively identical across all tiers — **1.1 days** for SILVER, GOLD, and PLATINUM alike. Premium tier status doesn't correspond to faster fulfillment in this dataset.

**Most profitable orders**: The top single-order profit was $3,214.80 (two separate $6,382.00 orders with identical cost structure), suggesting a specific high-margin product or bundle drives the highest-profit transactions.

**Best-selling product**: Product `240100300006` leads in units sold (1,700 units) but only generates $89,570.50 in revenue — well below several lower-volume products like `230100700008`, which sold fewer units (1,078) but generated **$551,186.60**, the highest revenue of any single product. This is a strong indicator that unit volume and revenue leadership don't align — a few high-price products drive disproportionate revenue despite moderate sales volume.

**Data quality note**: 427 warnings were generated during the CSV import (mostly minor formatting inconsistencies in the raw file), and standardizing `customer_status` casing changed 148,011 of 185,013 rows — meaning nearly 80% of records originally had inconsistent capitalization (e.g. `Silver` vs `SILVER`) before cleaning.

## 📁 Repository Contents
```
├── orders.csv                  # Dataset
├── orders_analysis.sql         # All SQL scripts (schema, cleaning, queries)
├── query_results/               # Screenshots or exported results of key queries
└── README.md                    # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open MySQL Workbench or the MySQL CLI
3. Run `orders_analysis.sql` top to bottom (or section by section)
4. Update the file path in the `LOAD DATA LOCAL INFILE` statement to match where `orders.csv` sits on your machine
5. If `local_infile` is disabled, enable it with `SET GLOBAL local_infile = 1;` and reconnect using `mysql --local-infile=1`

## ✅ Final Outcome
This task built practical SQL skills for data analysis — writing queries to retrieve, filter, sort, and aggregate structured data, along with real-world data cleaning (fixing date formats and inconsistent categorical values) that's essential before any meaningful analysis can happen.
