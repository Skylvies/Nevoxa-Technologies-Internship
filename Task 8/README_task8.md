# Portfolio Data — Excel Analysis & Dashboard (Task 8)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 8**. It uses Microsoft Excel to clean, analyze, and visualize daily price data for four assets (Amazon, Domino's, Bitcoin, Netflix), applying Pivot Tables, Pivot Charts, key Excel functions, Conditional Formatting, and an interactive slicer-driven dashboard.

## 📂 Dataset
**File:** `portfolio_data.csv`
**Records:** 1,520 rows, 5 columns
**Columns:**
| Column | Description |
|---|---|
| `Date` | Trading date |
| `AMZN` | Amazon closing price |
| `DPZ` | Domino's Pizza closing price |
| `BTC` | Bitcoin closing price |
| `NFLX` | Netflix closing price |

Data spans **2013–2019**, with no missing values or duplicate records.

## 🛠 Tools Used
- Microsoft Excel (Excel Online)
- Pivot Tables & Pivot Charts
- Excel Functions: IF, SUMIF, COUNTIF, XLOOKUP, INDEX-MATCH
- Conditional Formatting (Color Scales, Icon Sets, Highlight Rules)
- Slicers

## 🔍 Steps Performed
1. Imported the CSV into Excel and set up a `RawData` sheet
2. Verified no missing values or duplicates
3. Added derived columns: `Year`, `Month`, `Quarter`, `AMZN Change %`, `BTC Change %`, `Volatility Flag`
4. Applied core Excel functions:
   - **IF()** — flagged days with >5% BTC price swings as "High Volatility"
   - **SUMIF()** — summed AMZN closing prices for 2015
   - **COUNTIF()** — counted days BTC closed above $1,000
   - **XLOOKUP()** and **INDEX-MATCH** — looked up asset prices for a specific date (with a real troubleshooting fix: the Date column had a text/number mismatch, resolved by forcing values through `VALUE()`)
5. Built two Pivot Tables: Average Price by Year, and Average BTC Price by Quarter
6. Created two Pivot/Line Charts visualizing both views
7. Applied Conditional Formatting: color scale on BTC prices, icon sets on daily % change columns, highlight rule on the Volatility Flag column
8. Added a Slicer (Year) connected to both Pivot Tables for interactive filtering
9. Built a dedicated `Dashboard` sheet with KPI summary cells and both charts

## 📊 Key Insights
- **Bitcoin's price ranged from $69.66 to $18,972.32** across the dataset — a roughly 272x increase from its low, driven by the well-documented late-2017/early-2018 crypto boom.
- **BTC closed above $1,000 on 579 of the 1,520 trading days** (~38% of the dataset), concentrated almost entirely in 2017 onward — prior years rarely broke four figures.
- **Quarterly BTC data reveals the full boom-and-bust arc**: relatively flat pricing through 2016, a sharp climb through 2017 (Q4 2017 average ~$9,360), peaking around Q1 2018 (~$10,370), followed by a steady decline through 2018 into a 2019 partial rebound.
- **AMZN grew 721.6%** from its dataset minimum to maximum — strong, steady growth with none of BTC's extreme volatility.
- **Total AMZN closing price sum for 2015 was $120,490.85** (summed across all trading days that year) — a useful SUMIF-based aggregate for year-specific analysis.
- DPZ and NFLX remained comparatively low and stable throughout the period relative to BTC's scale, which is visually apparent when all four assets are plotted together — BTC's dramatic swing dwarfs the other three.

## 📁 Repository Contents
```
├── portfolio_data.csv              # Dataset
├── portfolio_dashboard.xlsx        # Excel workbook (RawData, PivotByYear,
│                                      PivotByQuarter, Dashboard sheets)
├── portfolio_dashboard_report.pdf  # Exported dashboard report
├── dashboard_screenshot.png        # Screenshot of the Dashboard sheet
└── README.md                       # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open `portfolio_dashboard.xlsx` in Microsoft Excel (desktop or Excel Online)
3. Explore the `RawData` sheet for the cleaned data and formulas
4. View `PivotByYear` and `PivotByQuarter` for the Pivot Tables, Charts, and Year slicer
5. View the `Dashboard` sheet for the consolidated KPI summary and charts

## ✅ Final Outcome
This task built practical Excel skills central to data analyst work — cleaning and structuring raw data, applying lookup and conditional functions, summarizing data through Pivot Tables, visualizing trends with Pivot Charts, and packaging findings into an interactive, filterable dashboard.
