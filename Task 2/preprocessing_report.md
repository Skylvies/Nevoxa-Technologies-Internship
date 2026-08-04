# Data Preprocessing Report — Housing Dataset

**Submitted for:** Novexa Technologies — Data Analysis Task 2
**Tools used:** Python, Pandas, NumPy, Scikit-learn

---

## 1. Introduction
The goal of this task was to clean and preprocess a raw dataset to prepare it for analysis and predictive modeling. The dataset used contains housing data with 545 records across 13 features, mixing numeric attributes (price, area, bedrooms) with categorical attributes (mainroad, furnishingstatus, etc.).

## 2. Dataset Overview
- **Rows:** 545
- **Columns:** 13 — 6 numeric, 6 binary categorical, 1 multi-class categorical
- **Target-like variable:** `price` (commonly used for regression modeling on this dataset)

## 3. Missing Values & Duplicates
| Check | Result |
|---|---|
| Missing values | None found across all 13 columns |
| Duplicate rows | None found |

Although this dataset happened to be clean, both checks were performed explicitly as a standard first step in any preprocessing pipeline — real-world data pulled from production systems is far less likely to be this tidy, so this step should never be skipped.

## 4. Outlier Detection
Outliers were identified using the **Interquartile Range (IQR) method**: any value below `Q1 - 1.5×IQR` or above `Q3 + 1.5×IQR` was flagged.

| Column | Outliers Found |
|---|---|
| `price` | 15 |
| `area` | 12 |
| `bedrooms` | 12 |
| `bathrooms` | 1 |
| `stories` | 41 |
| `parking` | 12 |

`stories` had by far the highest number of flagged outliers (41), largely because it's a small-range discrete variable (1–4), which makes the IQR method more sensitive to less common values like 4-story houses.

**Handling approach:** Rather than dropping outlier rows (which would shrink an already modest 545-row dataset), values were **capped** at the IQR lower/upper bounds. This preserves all 545 records while reducing the influence of extreme values.

## 5. Feature Encoding
Two encoding strategies were used based on the nature of each categorical variable:

| Encoding Type | Applied To | Reason |
|---|---|---|
| **Label Encoding** | `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea` | Binary yes/no values map cleanly to 0/1 with no risk of implying false order |
| **One-Hot Encoding** | `furnishingstatus` | 3 categories (furnished, semi-furnished, unfurnished) with no natural ranking — Label Encoding here would incorrectly imply one category is "greater than" another |

## 6. Feature Scaling
Numeric columns (`price`, `area`, `bedrooms`, `bathrooms`, `stories`, `parking`) were standardized using **StandardScaler** (mean = 0, standard deviation = 1). This is particularly important for `price` and `area`, which are on vastly different scales (price in millions, area in thousands) compared to `bedrooms` or `bathrooms` (single digits) — without scaling, models sensitive to feature magnitude (e.g. distance-based algorithms) would be dominated by `price` and `area` alone.

## 7. Key Findings
1. The dataset required no missing-value imputation or deduplication, but did require meaningful outlier and encoding work.
2. `stories` was the most outlier-prone numeric feature.
3. Choosing encoding method by data type mattered: binary vs. multi-class categorical variables were treated differently to avoid introducing false ordinal relationships.
4. Post-scaling, all numeric features are on a comparable scale, making the dataset suitable for both distance-based and gradient-based machine learning models.

## 8. Conclusion
This task reinforced the core preprocessing pipeline required before predictive modeling: verifying data quality (missing values, duplicates), handling outliers without discarding data, applying the correct encoding strategy per variable type, and scaling numeric features. The resulting `Housing_cleaned.csv` is ready for downstream regression or classification tasks.
