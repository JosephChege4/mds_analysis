# 🏥 Nursing Facility Risk Assessment & Quality Dashboard

## Overview

This project builds an end-to-end data analytics pipeline to assess and visualize nursing home performance in the U.S. using publicly available datasets from CMS (Centers for Medicare & Medicaid Services). By analyzing staffing, penalties, quality scores, and citations, this system aims to proactively identify high-risk facilities—empowering nursing home staff and owners to improve care, reduce penalties, and prevent compliance violations.

---

## Project Objectives

* Ingest and clean a variety of CMS datasets using their APIs.
* Analyze relationships between staffing, quality measures, survey citations, and financial penalties.
* Build interpretable ML models to predict:

  * Risk of receiving penalties or fines
  * Poor performance on quality measures
* Visualize key insights through a Power BI dashboard to:

  * Support healthcare compliance strategy
  * Enable better decision-making for nursing home stakeholders

---

## Tech Stack

### Programming & Analysis

* Python (Data Cleaning, API Calls, ML)
* SQL (via SQLAlchemy or pandas for in-memory operations)
* Power BI (for visualization)
* Jupyter Notebooks (for prototyping and EDA)

### Key Libraries

* `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
* `requests`, `json` (for CMS API access)
* `shap`, `joblib` (for model interpretation and storage)
* `PyMongo` (optional for storing cleaned datasets)

---

## 📁 Project Structure

```
nursing-facility-analytics/
├── data/                    # Sample subset of data
├── notebooks/               # Jupyter Notebooks for EDA and cleaning
│   └── 01_data_cleaning.ipynb
├── scripts/                 # Python scripts for data handling
│   ├── __init__.py
│   ├── fetch_data.py        # API-based data fetch and storage
│   └── clean_utils.py       # Custom data cleaning functions
├── models/                  # Trained models and SHAP explainability outputs
├── dashboards/              # Power BI dashboard (.pbix) and/or description
├── requirements.txt         # Dependencies
├── README.md                # Project overview
└── LICENSE                  # GNU GPL v3 License
```

---

## Data Sources and API Endpoints

CMS APIs are accessed in JSON format using `GET /provider-data/api/1/datastore/query/{distributionId}`. Two additional datasets use dedicated JSON endpoints. This design enables consistent data ingestion across all sources.

### Datasets Used (19 Total)

From [CMS Nursing Homes Portal](https://data.cms.gov/provider-data/topics/nursing-homes):

1. **Provider Information**
2. **MDS Quality Measures**
3. **Penalties**
4. **State-Level Health Inspection Cut Points**
5. **Fire Safety Deficiencies**
6. **Medicare Claims Quality Measures**
7. **Inspection Dates**
8. **Survey Summary**
9. **State US Averages**
10. **Ownership**
11. **FY 2025 SNF VBP Facility-Level Dataset**
12. **FY 2025 SNF VBP Aggregate Performance**
13. **Health Deficiencies**
14. **Nursing Home Data Collection Intervals**
15. **Skilled Nursing Facility Quality Reporting Program - National Data**
16. **Skilled Nursing Facility QRP - Swing Beds - Provider Data**
17. **Skilled Nursing Facility QRP - Provider Data**

From [CMS Quality of Care Portal](https://data.cms.gov/quality-of-care):

18. **Facility-Level Minimum Data Set Frequency**
19. **Minimum Data Set Frequency**

---

## Workflow Summary

1. **Data Ingestion**

   * Retrieve JSON data via CMS API endpoints
   * Store snapshots in `data/` or persist in `MongoDB` (optional)

2. **Cleaning & Standardization**

   * Normalize column names, parse dates, fill missing values
   * Join on `provider_id`, `federal_provider_number`, or similar keys

3. **Feature Engineering**

   * Construct:

     * Staff-to-resident ratios
     * Penalty rate metrics
     * Quality measure aggregates
     * Rolling scores and state comparisons

4. **Exploratory Data Analysis**

   * Identify trends, correlations, and outliers
   * Visualize state-by-state or ownership-type breakdowns

5. **Modeling & Risk Prediction**

   * Classify facilities as “at-risk” based on citations or fines
   * Use SHAP to interpret model predictions

6. **Dashboarding (Power BI)**

   * Dynamic filters (state, ownership, year)
   * Drill-down by facility
   * KPIs, risk heatmaps, penalty timelines

---

## Dashboard Preview

> *Coming soon* — a snapshot of the interactive Power BI dashboard will be included.

Expected sections:

* Risk Indicator Map
* Staffing vs Quality Bubble Chart
* Quality Score Trends
* Facility Scorecards

---

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/JosephChege4/nursing-facility-analytics.git
   cd nursing-facility-analytics
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Run data ingestion:

   ```bash
   python scripts/fetch_data.py
   ```

5. Open and run notebooks for cleaning and EDA.

---

## Future Work

* Integrate with **Flask/FastAPI** to deploy a facility lookup web tool.
* Add **LLM-based querying** for natural language analysis.
* Extend to real-time dashboards with APIs or direct facility reporting.
* Benchmark facility performance against national/state standards.

---

## License

Distributed under the [GNU General Public License v3.0](LICENSE).

---

## Contributing

Feel free to fork this repository, open issues, or submit pull requests for improvements.

---

## Author

**Joseph Chege Munga**

Math & CS Graduate | Python, ML, Data Science

GitHub: [@JosephChege4](https://github.com/JosephChege4)

Email: [chegejrmungai@gmail.com](mailto:chegejrmungai@gmail.com)