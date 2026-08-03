# Netflix Titles — Data Analysis (Task 1)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 1**. It applies core data analysis techniques using Python — loading, inspecting, cleaning, and visualizing a real-world dataset to extract meaningful insights.

## 📂 Dataset
**File:** `netflix.csv`
**Records:** 1000 rows, 7 columns
**Columns:**
| Column | Description |
|---|---|
| `title` | Name of the movie/show |
| `rating` | Content rating (e.g. PG-13, TV-MA, R) |
| `ratinglevel` | Text description of the rating (audience guidance) |
| `ratingdescription` | Numeric content score associated with the rating |
| `release_year` | Year the title was released |
| `user_rating_score` | User rating score (0–100 scale) |
| `user_rating_size` | Secondary user rating metric |

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab

## 🔍 Steps Performed
1. Loaded the dataset with `pandas.read_csv()`
2. Inspected structure using `.info()`, `.describe()`, `.head()`, `.tail()`
3. Identified missing values in `ratinglevel` (~5.9%) and `user_rating_score` (~39.5%)
4. Handled missing values — categorical gaps filled with `"Not Specified"`, numeric gaps filled with the median
5. Detected and removed **500 exact duplicate rows** (dataset had every record repeated twice, reducing 1000 → 500 unique rows)
6. Performed exploratory data analysis (EDA) with grouping and correlation checks
7. Visualized findings using bar charts, histograms, line charts, boxplots, and a correlation heatmap

## 📊 Key Insights
- The dataset contained **500 unique titles** after removing duplicates.
- **TV-14** is the most common content rating, followed by **TV-MA** and **PG**.
- Titles span release years from **1940 to 2017**, with a sharp concentration from **2013–2017** — 2016 alone accounts for the largest share of titles, suggesting the catalog is weighted toward recent content.
- Average `user_rating_score` is **~84.6** (median 88), indicating most titles are rated fairly positively.
- Correlation analysis shows only weak relationships between numeric fields (e.g. `release_year` vs `user_rating_score` ≈ 0.17), meaning newer titles aren't strongly associated with higher user ratings in this dataset.
- Nearly **40% of `user_rating_score` values were missing**, which is significant enough that any score-based conclusions should be treated as directional, not exact.

## 📁 Repository Contents
```
├── netflix.csv                     # Dataset
├── netflix_analysis.ipynb          # Jupyter/Colab notebook with full code
├── analysis_report.md              # Detailed analysis report
├── visuals/                        # Exported chart images (optional)
└── README.md                       # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open `netflix_analysis.ipynb` in Jupyter Notebook or upload it to Google Colab
3. Ensure `netflix.csv` is in the same directory (or upload it when prompted in Colab)
4. Run all cells sequentially

## ✅ Final Outcome
This task strengthened understanding of the full data analysis workflow — loading, cleaning, exploring, and visualizing data — as a foundation for future Data Science and Machine Learning work.
