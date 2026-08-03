# Data Analysis Report — Netflix Titles Dataset

**Submitted for:** Novexa Technologies — Data Analysis Task 1
**Tools used:** Python, Pandas, NumPy, Matplotlib, Seaborn

---

## 1. Introduction
The goal of this task was to perform a complete data analysis workflow on a real-world dataset — loading, inspecting, cleaning, and visualizing data to draw meaningful conclusions. The dataset used contains information on 1000 Netflix titles, including their content rating, release year, and user rating scores.

## 2. Dataset Overview
- **Rows (original):** 1000
- **Columns:** 7 — `title`, `rating`, `ratinglevel`, `ratingdescription`, `release_year`, `user_rating_score`, `user_rating_size`
- **Data types:** Mix of text (title, rating, ratinglevel) and numeric (ratingdescription, release_year, user_rating_score, user_rating_size)

## 3. Data Cleaning
Two issues were identified during inspection:

| Issue | Detail | Action Taken |
|---|---|---|
| Missing values | `ratinglevel` missing in 59 rows (~5.9%); `user_rating_score` missing in 395 rows (~39.5%) | Filled `ratinglevel` with `"Not Specified"`; filled `user_rating_score` with the column median (robust to outliers) |
| Duplicate rows | 500 rows were exact duplicates of other rows | Removed using `drop_duplicates()`, reducing the dataset from 1000 to 500 unique records |

The high proportion of missing `user_rating_score` values (~40%) is worth flagging — conclusions drawn from this column should be considered directional rather than precise.

## 4. Exploratory Data Analysis

### 4.1 Content Rating Distribution
`TV-14` is the most frequent content rating (106 titles), followed by `TV-MA` (82) and `PG` (76). This suggests the catalog skews toward content aimed at teens and mature audiences rather than young children.

### 4.2 Release Year Trends
Titles span release years from **1940 to 2017**. The distribution is heavily skewed toward recent years — **2016 alone contributes 146 titles**, with a clear ramp-up from 2013 onward. This points to significant catalog growth in the years just before the data was collected.

### 4.3 User Rating Scores
- **Mean:** 84.6
- **Median:** 88.0

The gap between mean and median suggests a left-skewed distribution — a cluster of lower-scoring titles pulls the average down while most titles sit in the high-80s to 90s range.

### 4.4 Correlation Analysis
| | ratingdescription | release_year | user_rating_score | user_rating_size |
|---|---|---|---|---|
| **ratingdescription** | 1.00 | 0.36 | 0.11 | -0.18 |
| **release_year** | 0.36 | 1.00 | 0.17 | 0.06 |
| **user_rating_score** | 0.11 | 0.17 | 1.00 | 0.11 |
| **user_rating_size** | -0.18 | 0.06 | 0.11 | 1.00 |

All correlations between numeric features are weak (below 0.4), indicating no strong linear relationships. Notably, `release_year` and `user_rating_score` are only weakly correlated (0.17) — newer titles are not meaningfully rated higher or lower than older ones in this dataset.

## 5. Key Findings
1. The dataset had a significant duplication issue — every record appeared exactly twice, which would double-count any statistic if not caught early.
2. Missing data was concentrated in `user_rating_score`, affecting nearly 40% of records.
3. The catalog is weighted toward mature-audience content (TV-14, TV-MA) and toward recent releases (post-2013).
4. User rating scores are generally high (median 88) but show no strong relationship with release year or content rating.

## 6. Conclusion
This analysis demonstrates the importance of thorough data cleaning before drawing conclusions — particularly catching duplicate records and quantifying missing data — since both issues were substantial in this dataset. The techniques applied here (structure inspection, missing value handling, deduplication, grouping, and correlation analysis) form a solid foundation for more advanced Data Science and Machine Learning tasks.
