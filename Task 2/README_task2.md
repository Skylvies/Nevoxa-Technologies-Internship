# Housing Dataset — Data Cleaning & Preprocessing (Task 2)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 2**. It focuses on data cleaning and preprocessing — handling missing values, duplicates, outliers, categorical encoding, and feature scaling — to prepare a dataset suitable for predictive modeling.

## 📂 Dataset
**File:** `Housing.csv`
**Records:** 545 rows, 13 columns
**Columns:**
| Column | Type | Description |
|---|---|---|
| `price` | Numeric | House price (target variable) |
| `area` | Numeric | Plot/house area |
| `bedrooms` | Numeric | Number of bedrooms |
| `bathrooms` | Numeric | Number of bathrooms |
| `stories` | Numeric | Number of stories |
| `mainroad` | Categorical (binary) | Whether the house faces a main road |
| `guestroom` | Categorical (binary) | Whether a guestroom is available |
| `basement` | Categorical (binary) | Whether a basement is available |
| `hotwaterheating` | Categorical (binary) | Whether hot water heating is available |
| `airconditioning` | Categorical (binary) | Whether air conditioning is available |
| `parking` | Numeric | Number of parking spots |
| `prefarea` | Categorical (binary) | Whether located in a preferred area |
| `furnishingstatus` | Categorical (3-class) | furnished / semi-furnished / unfurnished |

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab

## 🔍 Steps Performed
1. Loaded the dataset with `pandas.read_csv()`
2. Inspected structure using `.info()`, `.describe()`, `.head()`
3. Checked for missing values — **none found**
4. Checked for duplicate rows — **none found**
5. Detected outliers in numeric columns using the **IQR method**
6. Capped outliers using the IQR bounds (preserves data volume vs. dropping rows)
7. Applied **Label Encoding** to 6 binary categorical columns (`mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`)
8. Applied **One-Hot Encoding** to `furnishingstatus` (3 categories, no natural order)
9. Applied **Standard Scaling** to numeric columns (`price`, `area`, `bedrooms`, `bathrooms`, `stories`, `parking`)
10. Exported the cleaned, encoded, and scaled dataset as `Housing_cleaned.csv`

## 📊 Key Findings
- The dataset was already free of missing values and duplicate records.
- Outliers were present in **price** (15), **area** (12), **stories** (41), **bedrooms** (12), and **parking** (12) — `stories` had the highest proportion of outliers.
- All 6 binary categorical columns follow a simple `yes`/`no` pattern, making Label Encoding appropriate.
- `furnishingstatus` has no inherent order between its 3 categories, so One-Hot Encoding was used instead of Label Encoding to avoid implying a false ranking.

## 📁 Repository Contents
```
├── Housing.csv                     # Original dataset
├── Housing_cleaned.csv             # Cleaned, encoded, and scaled dataset
├── housing_preprocessing.ipynb     # Jupyter/Colab notebook with full code
├── preprocessing_report.md         # Detailed preprocessing report
└── README.md                       # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open `housing_preprocessing.ipynb` in Jupyter Notebook or upload it to Google Colab
3. Ensure `Housing.csv` is in the same directory (or upload it when prompted in Colab)
4. Run all cells sequentially

## ✅ Final Outcome
This task built practical experience in preparing raw data for machine learning — covering outlier handling, encoding strategies for different types of categorical data, and feature scaling — as a foundation for predictive modeling tasks.
