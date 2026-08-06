# Healthcare Dataset — Exploratory Data Analysis (Task 3)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 3**. It performs Exploratory Data Analysis (EDA) on a healthcare dataset to uncover patterns, trends, relationships, and data quality issues that could support business decisions or downstream machine learning work.

## 📂 Dataset
**File:** `healthcare_dataset.csv`
**Records:** 55,500 rows, 15 columns
**Columns:**
| Column | Type | Description |
|---|---|---|
| `Name` | Text | Patient name |
| `Age` | Numeric | Patient age (13–89) |
| `Gender` | Categorical | Male / Female |
| `Blood Type` | Categorical | 8 blood type groups |
| `Medical Condition` | Categorical | Diagnosis (6 categories: Cancer, Obesity, Diabetes, Asthma, Hypertension, Arthritis) |
| `Date of Admission` | Date | Admission date |
| `Doctor` | Text | Attending doctor |
| `Hospital` | Text | Hospital name |
| `Insurance Provider` | Categorical | 5 insurance providers |
| `Billing Amount` | Numeric | Billed amount for treatment |
| `Room Number` | Numeric | Assigned room number |
| `Admission Type` | Categorical | Elective / Urgent / Emergency |
| `Discharge Date` | Date | Discharge date |
| `Medication` | Categorical | Prescribed medication |
| `Test Results` | Categorical | Normal / Abnormal / Inconclusive |

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
3. Checked for missing values — **none found**
4. Identified and removed **534 duplicate rows**
5. Discovered and corrected a data quality issue: **108 rows had negative `Billing Amount` values**, converted to absolute values
6. Performed univariate analysis (age distribution, condition frequency, billing distribution)
7. Performed bivariate analysis (billing by condition, admission type vs test results, condition by gender)
8. Performed multivariate analysis (correlation matrix, age vs billing colored by test result)
9. Detected outliers in `Billing Amount` using the IQR method

## 📊 Key Insights
- The dataset is **evenly distributed across genders** (27,774 Male vs 27,726 Female) and fairly evenly across all 6 medical conditions (~9,200 each).
- A **data quality issue** was found: 108 records had negative billing amounts, which is not logically valid for a billed amount — corrected by taking absolute values.
- Average billing amount is broadly similar across medical conditions (~$25,000–$25,800), with **Obesity** having the highest average billing and **Cancer** the lowest — differences are modest, suggesting billing is not strongly condition-driven in this dataset.
- **Age shows almost no correlation with Billing Amount** (correlation ≈ -0.003), meaning older patients are not billed systematically more or less than younger ones.
- Admission types (Elective, Urgent, Emergency) are nearly evenly split (~18,300–18,700 each), and test results (Normal, Abnormal, Inconclusive) are similarly balanced.

## 📁 Repository Contents
```
├── healthcare_dataset.csv          # Dataset
├── healthcare_eda.ipynb            # Jupyter/Colab notebook with full code
├── eda_report.md                   # Detailed EDA report
├── visuals/                        # Exported chart images (optional)
└── README.md                       # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open `healthcare_eda.ipynb` in Jupyter Notebook or upload it to Google Colab
3. Ensure `healthcare_dataset.csv` is in the same directory (or upload it when prompted in Colab)
4. Run all cells sequentially

## ✅ Final Outcome
This task built practical experience in exploratory data analysis — using univariate, bivariate, and multivariate techniques to uncover patterns, spot data quality issues, and generate insights that would inform both business reporting and any future machine learning work on this dataset.
