# Task 12: Data Analysis Using Python and SQL

## Novexa Technologies – Data Analyst Internship

### Overview
This project analyzes a retail sales dataset using SQL and Python together — data was
loaded into a SQL database, queried using SQL, and the results were analyzed and
visualized in Python (Pandas, Matplotlib, Seaborn).

### Tools Used
- Python (Pandas, Matplotlib, Seaborn)
- SQL (MySQL Workbench for schema design; SQLite for the Python integration in Colab)
- Jupyter Notebook (Google Colab)

### Repository Contents
| File | Description |
|------|-------------|
| `retail_sales_dataset.csv` | Raw dataset used for the analysis |
| `queries.sql` | SQL queries used to extract business insights |
| `retail_analysis.ipynb` | Jupyter notebook with data loading, SQL integration, cleaning, and visualizations |
| `category_revenue.png` | Chart of total revenue by product category |

### Approach
1. Imported the dataset into a SQL database (MySQL Workbench for schema/queries;
   SQLite used in the notebook for a portable Python–SQL connection).
2. Connected Python to the database using `sqlite3` / `SQLAlchemy`.
3. Ran SQL queries (`GROUP BY`, aggregations) and loaded results into Pandas DataFrames
   using `pd.read_sql_query()`.
4. Cleaned and explored the data (checked nulls, duplicates, data types).
5. Performed business analysis:
   - Total revenue by product category
   - Top 10 customers by spend
   - Monthly revenue trend
   - Revenue breakdown by gender
6. Visualized results using Matplotlib and Seaborn.

### Key Insights
- Identified the top-performing product categories by revenue.
- Found the highest-spending customers.
- Observed monthly revenue trends across the year.
- Compared revenue and transaction volume across genders.

### How to Run
1. Clone this repository.
2. Open `retail_analysis.ipynb` in Jupyter Notebook or Google Colab.
3. Run all cells to reproduce the SQL queries, DataFrames, and visualizations.

### Author
Sky
