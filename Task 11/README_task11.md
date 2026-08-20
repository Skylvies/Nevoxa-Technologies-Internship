# Healthcare Operations — Tableau Dashboard (Task 11)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 11**. It uses Tableau Public to build an interactive exploratory dashboard on healthcare patient data, covering calculated fields, multiple chart types (including a treemap), and cross-filtering interactivity.

## 📂 Dataset
**File:** `healthcare_dataset.csv`
**Records:** 55,500 rows, 15 columns
**Key fields:** Age, Gender, Medical Condition, Admission Type, Billing Amount, Date of Admission, Discharge Date, Test Results, Insurance Provider

## 🛠 Tools Used
- Tableau Public Desktop

## 🔍 Steps Performed
1. Connected `healthcare_dataset.csv` to Tableau Public and verified data types (dates, numbers, text)
2. Created calculated fields:
   - `Billing Amount (Fixed)` — corrects invalid negative billing values using `ABS([Billing Amount])`
   - `Length of Stay` — derived from `DATEDIFF('day', [Date of Admission], [Discharge Date])`
3. Built five worksheets:
   - **Billing by Condition** — average billing amount per medical condition
   - **Length of Stay by Condition** — average length of stay per medical condition
   - **Admission Type Volume** — patient count by admission type
   - **Billing Treemap** — medical condition billing visualized as a treemap
   - **Test Results Breakdown** — pie chart of test result distribution
4. Assembled all five into a single interactive **Dashboard**
5. Added a Medical Condition filter applied across all worksheets for cross-chart interactivity
6. Set a fixed dashboard size and added a dashboard title

## 📊 Key Insights
- **Billing is nearly uniform across medical conditions** — all six conditions average close to $25,000–26,000, visible clearly in both the bar chart and the treemap, where rectangle sizes look almost identical across conditions rather than showing one condition dominating.
- **Length of stay shows the same pattern** — averaging roughly 15–16 days regardless of condition, suggesting a standardized care pathway rather than condition-driven treatment duration.
- **Admission volume is split almost evenly** across Elective, Emergency, and Urgent types, each accounting for close to a third of all patients.
- **Test results are similarly balanced** across Abnormal, Normal, and Inconclusive outcomes in the pie chart.
- The **interactive filter** lets a user click any medical condition and instantly see how billing, length of stay, admission type, and test results shift for that specific condition — useful for spotting whether any single condition deviates from the otherwise uniform patterns above.

## 📁 Repository Contents
```
├── healthcare_dataset.csv                     # Dataset
├── Healthcare_Operations_Dashboard.twbx        # Tableau packaged workbook
└── README.md                                   # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Open `Healthcare_Operations_Dashboard.twbx` in Tableau Public Desktop (or Tableau Desktop)
3. Use the Medical Condition filter on the dashboard to explore how metrics change per condition

## ✅ Final Outcome
This task built practical experience with Tableau — connecting and cleaning data through calculated fields, choosing chart types suited to different questions (bar charts for comparison, a treemap for proportional billing, a pie chart for distribution), and assembling everything into a single interactive dashboard using cross-filtering.
