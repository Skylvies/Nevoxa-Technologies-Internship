# Exploratory Data Analysis Report — Healthcare Dataset

**Submitted for:** Novexa Technologies — Data Analysis Task 3
**Tools used:** Python, Pandas, NumPy, Matplotlib, Seaborn

---

## 1. Introduction
The goal of this task was to perform Exploratory Data Analysis (EDA) on a healthcare dataset to uncover patterns, trends, and relationships across patient demographics, medical conditions, and billing information, while also identifying data quality issues.

## 2. Dataset Overview
- **Rows (original):** 55,500
- **Columns:** 15 — mixing patient demographics, medical details, and billing/administrative fields
- **Key numeric fields:** `Age`, `Billing Amount`, `Room Number`
- **Key categorical fields:** `Gender`, `Blood Type`, `Medical Condition`, `Insurance Provider`, `Admission Type`, `Test Results`

## 3. Data Quality Checks

| Check | Result | Action Taken |
|---|---|---|
| Missing values | None found | No action needed |
| Duplicate rows | 534 duplicate rows found | Removed via `drop_duplicates()`, reducing dataset to 54,966 rows |
| Invalid values | 108 rows had **negative** `Billing Amount` | Converted to absolute values, since a billed amount cannot logically be negative |

The negative billing amounts are the most notable data quality finding — this kind of issue is easy to miss if you only check `.isnull()` and skip sanity-checking value ranges for fields that have real-world constraints (like billing amounts always being ≥ 0).

## 4. Univariate Analysis
- **Age**: Patients range from 13 to 89 years old, roughly evenly spread with no strong skew toward a particular age group.
- **Medical Condition**: The 6 conditions (Cancer, Obesity, Diabetes, Asthma, Hypertension, Arthritis) are nearly evenly represented, each accounting for roughly 16–17% of records (~9,200 each).
- **Billing Amount**: Spread across a wide range with no extreme concentration at either end, following a roughly uniform-to-normal shape after correcting the negative values.

## 5. Bivariate Analysis
- **Billing Amount by Medical Condition**: Average billing ranges narrowly from **$25,152 (Cancer)** to **$25,804 (Obesity)** — a difference of only about 2.6%, suggesting billing amount is not strongly driven by diagnosis in this dataset.
- **Admission Type vs Test Results**: Cross-tabulation shows no dominant pairing — Urgent, Elective, and Emergency admissions are distributed similarly across Normal, Abnormal, and Inconclusive test outcomes.
- **Medical Condition by Gender**: Gender split is close to 50/50 within every medical condition category, indicating no gender skew in diagnosis representation in this dataset.

## 6. Multivariate Analysis
- **Correlation Matrix**: Numeric features (`Age`, `Billing Amount`, `Room Number`) show negligible correlation with each other (all values near 0), meaning none of these fields are useful linear predictors of one another.
- **Age vs Billing Amount by Test Result**: Scatter analysis shows no visible clustering pattern — billing amount appears effectively independent of both age and test outcome.

## 7. Outlier Detection
Using the IQR method on `Billing Amount`, a modest number of outliers were flagged on both the high and low ends. Given the earlier correction of negative values, these remaining outliers represent genuinely high or low (but valid) billing amounts rather than data entry errors, so they were left in place for analysis purposes rather than removed.

## 8. Key Findings
1. The dataset required deduplication (534 rows) and correction of a real data quality issue (108 negative billing values) before analysis could be trusted.
2. Demographics (age, gender) and medical conditions are all fairly evenly distributed — this appears to be a synthetically balanced dataset rather than a naturally skewed real-world sample.
3. Billing Amount shows **no meaningful correlation** with Age, Medical Condition, or Room Number, meaning billing in this dataset behaves close to randomly assigned rather than driven by patient or treatment characteristics.
4. Admission Type and Test Results show no strong dependency on each other.

## 9. Conclusion
This EDA surfaced a genuine data quality issue (negative billing values) that would have skewed any downstream financial analysis if left unchecked, alongside confirming that this particular dataset's billing figures don't correlate meaningfully with patient age, condition, or admission details. The near-uniform distribution across most categorical fields suggests this dataset is well-suited for practicing analysis and visualization techniques, though any billing-prediction modeling built on it would need additional real-world features to be meaningful.
