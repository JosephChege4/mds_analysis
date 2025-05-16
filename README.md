# Predictive Analytics & Dashboarding for Skilled Nursing Facility Residents

## Overview

This project focuses on analyzing and visualizing the Facility-Level Minimum Data Set (MDS) data provided by CMS to identify resident-level trends, risk profiles, and key insights across skilled nursing facilities. The goal is to build a robust data pipeline, predictive modeling layer, and an interactive Power BI dashboard to support healthcare compliance analytics.

## Project Objectives

* Preprocess and clean high-volume MDS healthcare data.
* Engineer features from cognitive, health, and functional metrics.
* Train interpretable machine learning models to cluster residents or predict risks.
* Develop a clear and functional Power BI dashboard to showcase insights.
* Provide extensible, production-ready code in Python and SQL.

## Tech Stack

* **Programming**: Python (Pandas, Numpy, Scikit-learn)
* **Data Storage**: SQL (via SQLAlchemy) or MongoDB (via PyMongo)
* **ML/Stats**: Scikit-learn, SHAP, Matplotlib/Seaborn
* **Visualization**: Power BI
* **Environment**: Jupyter, VS Code, GitHub

## Project Structure

```
├── data/                    # Cleaned data samples or schema
├── scripts/                 # Python scripts for data cleaning, modeling, 
├── models/                  # Trained models, SHAP outputs
├── powerbi/                 # .pbix file or dashboard description
├── requirements.txt         # Dependencies
├── README.md                # This file
└── LICENSE                  # GNU GPL v3 License
```

## Data Source

**Source**: [CMS.gov Facility-Level Minimum Data Set Frequency](https://data.cms.gov/quality-of-care/facility-level-minimum-data-set-frequency)

This dataset includes:

* Resident characteristics (age, race, marital status)
* Health indicators (diagnoses, cognitive/mood status)
* Medications and treatments
* Functional and behavioral metrics

Due to its size, the dataset is best processed using statistical software or a database.

## Workflow Summary

1. **Ingest Data**: Load raw CSV into a Pandas DataFrame or SQL database.
2. **Clean & Transform**: Handle missing values, encode categorical variables, standardize scales.
3. **Modeling**:

   * Cluster residents by health/function profiles.
   * Predict likelihood of outcomes (e.g., readmission).
   * Use SHAP for interpretability.
4. **Power BI Dashboard**:

   * Import cleaned/aggregated dataset.
   * Design visuals for clarity and interactivity.
   * Share or export as .pbix.

## Dashboard Preview

> \[Include a screenshot here of the Power BI dashboard once available. You can upload it to GitHub and link it using markdown.]

Key components:

* Resident risk profile summary
* Facility-level filtering
* Interactive drill-down by age group, diagnosis, etc.

## Setup Instructions

```bash
# Clone the repository
$ git clone https://github.com/JosephChege4/nursing-facility-analytics.git
$ cd nursing-facility-analytics

# Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
$ pip install -r requirements.txt

# Run initial ETL script
$ python scripts/clean_data.py
```

## Future Work

* Integrate time series modeling for resident trends.
* Build a REST API for querying ML results.
* Use LLMs to auto-generate patient summaries.
* Automate dashboard refresh with live data.
* Add HIPAA-safe data simulation tools for demonstration purposes.

## License

This project is licensed under the **GNU General Public License v3.0**. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please fork the repo and submit a pull request. For major changes, open an issue first to discuss what you'd like to change.

## Author

**\[Your Full Name]**
Recent NYU Graduate | Math & CS | Python & Data Science Enthusiast
GitHub: [@JosephChege4](https://github.com/JosephChege4)
