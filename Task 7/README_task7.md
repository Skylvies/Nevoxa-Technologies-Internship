# Amazon Sales — Business Intelligence Dashboard (Task 7)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 7**. It uses Microsoft Power BI to build an interactive business intelligence dashboard on Amazon e-commerce sales data — covering data cleaning with Power Query, DAX measures, KPI cards, and multiple visualization types with slicer-based interactivity.

## 📂 Dataset
**File:** `Amazon_Sale_Report.csv`
**Records:** 128,975 rows, 17 columns (after cleanup)
**Key columns:**
| Column | Description |
|---|---|
| `Order ID` | Unique order identifier |
| `Date` | Order date |
| `Status` | Order status (Shipped, Cancelled, Pending, etc.) |
| `Fulfilment` | Amazon or Merchant fulfilled |
| `Sales Channel` | Amazon.in / Non-Amazon |
| `Category` | Product category (Set, kurta, Western Dress, Top, etc.) |
| `Qty` | Units ordered |
| `Amount` | Order value |
| `ship-city` / `ship-state` | Shipping destination |
| `B2B` | Whether the order was business-to-business |

## 🛠 Tools Used
- Microsoft Power BI Desktop
- Power Query (data cleaning and transformation)
- DAX (measures and calculated columns)

## 🔍 Steps Performed
1. Imported the CSV into Power BI and opened Power Query Editor
2. Cleaned the data:
   - Removed unnecessary columns (`index`, `Unnamed: 22`, `fulfilled-by`, `promotion-ids`, `ASIN`, `SKU`, `Style`)
   - Converted `Date` from text to a proper Date type using a custom column formula (handling the `MM-DD-YY` raw format)
   - Replaced null `Amount` values (from Cancelled orders) with `0`
   - Replaced null `Courier Status` values with `"Not Shipped"`
   - Renamed `Sales Channel ` (trailing space) to `Sales Channel`
3. Created 6 DAX measures: Total Revenue, Total Orders, Total Units Sold, Cancelled Orders, Cancellation Rate, Average Order Value
4. Created a `Month Year` calculated column (with a `Month Sort` helper column) to enable clean chronological monthly trend visualization
5. Built the dashboard with KPI cards, a bar chart, a donut chart, a line chart, and a secondary bar chart
6. Added slicers for Date, Category, Sales Channel, and B2B to make the dashboard interactive

## 📊 Dashboard Components
- **KPI Cards**: Total Revenue, Total Orders, Total Units Sold, Cancelled Orders, Cancellation Rate, Average Order Value
- **Bar Chart**: Total Revenue by Category
- **Donut Chart**: Total Orders by Fulfilment Method
- **Line Chart**: Total Revenue by Month
- **Bar Chart**: Total Orders by Shipping State (Top 10)
- **Slicers**: Date (range), Category, Sales Channel, B2B

## 📈 Key Insights
- **Total Revenue: 78.59M** across **120K orders** (**117K units sold**), for an average order value of **652.88**.
- **Cancellation rate is 14%** (17K of 120K orders cancelled) — a meaningful chunk of order volume worth investigating from a business standpoint.
- **"Set" is the top revenue-generating category** (~$36–37M), followed closely by **"kurta"** (~$28M) — together these two categories account for the large majority of total revenue. "Western Dress" and "Top" trail well behind.
- **Amazon-fulfilled orders dominate at 69.78%** (84K orders) vs. **Merchant-fulfilled at 30.22%** (36K orders) — the business relies heavily on Amazon's own fulfillment infrastructure over third-party sellers.
- **Maharashtra and Karnataka are the top two shipping states** by order volume, followed by Tamil Nadu, Telangana, and Uttar Pradesh — indicating strong demand concentration in southern and western India.
- Revenue by month shows relative stability with modest fluctuation rather than dramatic seasonal spikes, based on the cleaned monthly trend line.

## 📁 Repository Contents
```
├── Amazon_Sale_Report.csv          # Dataset
├── Amazon_Sales_Dashboard.pbix     # Power BI dashboard file
├── Amazon_Sales_Dashboard.pdf      # Exported dashboard report
├── dashboard_screenshot.png        # Dashboard screenshot(s)
└── README.md                       # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open `Amazon_Sales_Dashboard.pbix` in Power BI Desktop (free download from Microsoft)
3. If prompted to refresh data, ensure `Amazon_Sale_Report.csv` is in the same directory, or update the data source path via **Transform Data → Data Source Settings**
4. Use the slicers (Date, Category, Sales Channel, B2B) to explore the data interactively

## ✅ Final Outcome
This task built hands-on experience with the full Business Intelligence workflow — cleaning and transforming raw data with Power Query, writing DAX measures for KPIs, and designing an interactive dashboard that supports real business decision-making through filters, slicers, and multiple coordinated visualizations.
