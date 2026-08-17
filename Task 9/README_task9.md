# Healthcare Operations & Billing — Data Storytelling Report (Task 9)

## 📌 Overview
This project is submitted for the **Novexa Technologies Data Analysis Task 9**. It converts raw healthcare admission data into a business-facing insights report and presentation — practicing data storytelling for both technical and non-technical audiences.

## 📂 Dataset
**File:** `healthcare_dataset.csv`
**Records:** 55,500 rows (54,966 after deduplication), 15 columns
**Key fields:** Age, Gender, Medical Condition, Admission Type, Billing Amount, Length of Stay (derived), Test Results, Insurance Provider

## 🛠 Tools Used
- Python (Pandas, Matplotlib, Seaborn) for analysis
- Microsoft Word for the business report
- Microsoft PowerPoint for the presentation

## 🔍 Business Objective
Hospital administrators and finance teams need to know whether billing and resource utilization (length of stay) vary meaningfully by patient condition, admission urgency, or insurance provider — to inform staffing, capacity planning, and insurer contract negotiations.

## 🔍 Steps Performed
1. Loaded and inspected the dataset
2. Cleaned the data: removed 534 duplicate rows, corrected 108 records with invalid negative billing values (converted to absolute value)
3. Derived a `Length of Stay` field from admission and discharge dates
4. Analyzed billing patterns by medical condition, admission type, and insurance provider
5. Analyzed length-of-stay patterns by medical condition
6. Built supporting visualizations for each finding
7. Wrote a full Business Insights Report translating statistical findings into business language and recommendations
8. Built a presentation deck condensing the report into a stakeholder-ready slide format

## 📊 Key Findings
- **Billing is remarkably uniform across medical conditions** — ranging from $25,154.73 (Cancer) to $25,806.63 (Obesity), only a 2.6% spread — suggesting flat-rate or bundled pricing rather than condition-driven cost structures.
- **Length of stay barely varies by condition** — all six conditions fall between 15.43 and 15.68 average days, pointing to a standardized discharge pathway.
- **Admission volume splits almost evenly three ways**: Elective (18,473), Urgent (18,391), Emergency (18,102) — emergency capacity planning should assume roughly one-third of total demand is unscheduled.
- **Test results are similarly balanced**: Abnormal (33.5%), Normal (33.3%), Inconclusive (33.1%).
- **Data quality issue identified and corrected**: 108 records (0.2%) had negative billing values before cleaning — a good example of why sanity-checking value ranges matters beyond just checking for nulls.
- **Total billed revenue across the dataset: $1,404,174,863**, averaging $25,546.24 per patient.

## 📁 Repository Contents
```
├── healthcare_dataset.csv                    # Dataset
├── Business_Insights_Report.pdf              # Full business report
├── Business_Insights_Presentation.pdf        # Stakeholder presentation slides
└── README.md                                  # Project overview (this file)
```

## 🚀 How to Run
1. Clone this repository
2. Review `Business_Insights_Report.pdf` for the full written analysis
3. Review `Business_Insights_Presentation.pdf` for the stakeholder-facing summary
4. Refer to `healthcare_dataset.csv` for the underlying raw data behind both documents

## ✅ Final Outcome
This task built practical experience in data storytelling — translating statistical findings (means, distributions, group comparisons) into business language, framing each finding around its operational implication, and packaging the same underlying analysis for two different audiences: a detailed written report and a concise stakeholder presentation.
