# COVID-19 Country-Wise Data — Data Visualization (Task 4)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 4**. It focuses on data visualization — using Matplotlib, Seaborn, and Plotly to create informative charts that reveal trends, patterns, distributions, and relationships in a COVID-19 country-level dataset.

## 📂 Dataset
**File:** `country_wise_latest.csv`
**Records:** 187 rows (countries), 15 columns
**Columns:**
| Column | Description |
|---|---|
| `Country/Region` | Country name |
| `Confirmed` | Total confirmed cases |
| `Deaths` | Total deaths |
| `Recovered` | Total recovered cases |
| `Active` | Currently active cases |
| `New cases` / `New deaths` / `New recovered` | Latest day's new counts |
| `Deaths / 100 Cases` | Death rate |
| `Recovered / 100 Cases` | Recovery rate |
| `Deaths / 100 Recovered` | Deaths relative to recoveries |
| `Confirmed last week` | Confirmed cases one week prior |
| `1 week change` / `1 week % increase` | Week-over-week change |
| `WHO Region` | WHO-designated region |

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly (for interactive charts)
- Google Colab

## 🔍 Steps Performed
1. Loaded the dataset with `pandas.read_csv()`
2. Explored structure using `.info()`, `.describe()`, `.head()`
3. Verified data quality — no missing values or duplicates found
4. Created bar charts for top countries by confirmed cases and deaths
5. Aggregated and visualized totals by WHO Region
6. Built distribution plots (histogram, boxplot) for death rate
7. Explored relationships using a log-scale scatter plot (Confirmed vs Deaths) and a correlation heatmap
8. Built interactive visualizations with Plotly — a global choropleth map and a top-15 recovery rate bar chart
9. Exported key charts as PNG images for the visualization report

## 📊 Key Insights
- **US, Brazil, and India** are the top 3 countries by confirmed cases, with the US leading by a wide margin (~4.29M confirmed).
- **Yemen** has the highest death rate at 28.56 deaths per 100 cases — far above any other country — followed by the United Kingdom, Belgium, Italy, and France in the 13–15% range.
- **Europe (56 countries)** and **Africa (48 countries)** have the most countries represented in the dataset, while **South-East Asia (10)** has the fewest.
- Death rate varies significantly by WHO Region, with some regions showing much wider spread (more inconsistency between countries) than others.
- There is a visible positive relationship between Confirmed cases and Deaths on a log scale, though countries deviate substantially from any single trend line — reflecting differences in healthcare capacity and reporting.

## 📁 Repository Contents
```
├── country_wise_latest.csv         # Dataset
├── covid_visualization.ipynb       # Jupyter/Colab notebook with full code
├── visualization_report.md         # Detailed visualization report
└── README.md                       # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open `covid_visualization.ipynb` in Jupyter Notebook or upload it to Google Colab
3. Ensure `country_wise_latest.csv` is in the same directory (or upload it when prompted in Colab)
4. Run all cells sequentially

## ✅ Final Outcome
This task built practical experience in choosing the right chart type for the right question — bar charts for rankings, histograms and boxplots for distributions, scatter plots and heatmaps for relationships, and interactive Plotly visuals for exploration — to communicate business-relevant insights clearly.
