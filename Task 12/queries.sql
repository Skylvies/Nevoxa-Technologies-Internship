-- category_revenue
SELECT "Product Category", SUM("Total Amount") AS total_revenue
FROM retail_sales
GROUP BY "Product Category"
ORDER BY total_revenue DESC;

-- top_customers
SELECT "Customer ID", SUM("Total Amount") AS total_spent
FROM retail_sales
GROUP BY "Customer ID"
ORDER BY total_spent DESC
LIMIT 10;

-- monthly_trend
SELECT strftime('%m', Date) AS month, SUM("Total Amount") AS revenue
FROM retail_sales
GROUP BY month
ORDER BY month;

-- gender_revenue
SELECT Gender, SUM("Total Amount") AS total_revenue, COUNT(*) AS transactions
FROM retail_sales
GROUP BY Gender;

