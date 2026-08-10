# Student Performance Dataset — Statistical Data Analysis (Task 5)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 5**. It applies descriptive and inferential statistical methods using Python to analyze student performance data, uncover relationships between variables, and draw statistically grounded conclusions.

## 📂 Dataset
**File:** `student_data.csv`
**Records:** 395 rows, 33 columns
**Key columns:**
| Column | Type | Description |
|---|---|---|
| `sex`, `age`, `address` | Categorical/Numeric | Student demographics |
| `Medu`, `Fedu` | Numeric | Mother's / Father's education level |
| `Mjob`, `Fjob` | Categorical | Mother's / Father's job |
| `studytime` | Numeric | Weekly study time (1–4 scale) |
| `failures` | Numeric | Number of past class failures |
| `absences` | Numeric | Number of school absences |
| `Dalc`, `Walc` | Numeric | Workday / Weekend alcohol consumption (1–5 scale) |
| `G1`, `G2`, `G3` | Numeric | First period, second period, and final grades (0–20 scale) |

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Google Colab

## 🔍 Steps Performed
1. Loaded the dataset with `pandas.read_csv()`
2. Explored structure using `.info()`, `.describe()`, `.head()`
3. Verified data quality — no missing values or duplicate rows found
4. Computed descriptive statistics (mean, median, mode, standard deviation, variance, range) for the final grade (`G3`)
5. Built a correlation matrix across all numeric features
6. Ran a **t-test** comparing final grades between male and female students
7. Ran a **one-way ANOVA** testing whether mother's job (`Mjob`) affects final grade
8. Visualized relationships using histograms, boxplots, a correlation heatmap, and regression scatter plots

## 📊 Key Insights
- **Final grade (G3)**: Mean = 10.42, Median = 11.0, Mode = 10, Standard Deviation ≈ 4.58 — a moderately wide spread around the middle of the 0–20 scale.
- **G1 and G2 strongly predict G3** (correlation of 0.80 and 0.91 respectively) — unsurprising, since they're earlier grading periods for the same students, but a useful confirmation that grades are consistent over time.
- **Study time has almost no correlation with final grade** (r ≈ 0.10) — a notable and slightly counterintuitive finding worth discussing in the report.
- **Gender difference is statistically significant**: male students scored higher on average (10.91 vs 9.97), with a t-test p-value of 0.0399 (below the 0.05 significance threshold).
- **Mother's education level (`Medu`)** shows a modest positive correlation with final grade (r ≈ 0.22), stronger than study time.

## 📁 Repository Contents
```
├── student_data.csv                # Dataset
├── student_statistical_analysis.ipynb  # Jupyter/Colab notebook with full code
└── README.md                       # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open `student_statistical_analysis.ipynb` in Jupyter Notebook or upload it to Google Colab
3. Ensure `student_data.csv` is in the same directory (or upload it when prompted in Colab)
4. Run all cells sequentially

## ✅ Final Outcome
This task built practical experience applying descriptive statistics (mean, median, mode, variance, standard deviation) and inferential statistics (t-tests, ANOVA, correlation analysis) to draw meaningful, evidence-based conclusions from data — a foundation for hypothesis-driven analysis in future Data Science and ML work.
