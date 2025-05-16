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
* **Environment**: Jupyter Notebook, GitHub, REST API

## Project Structure

```
├── data/                    # Sample subset of MDS data
├── notebooks/               # Jupyter Notebooks for EDA and cleaning
│   └── 01_data_cleaning.ipynb
├── scripts/                 # Python scripts for data handling
│   ├── __init__.py          # Centralizes imports
│   ├── fetch_data.py        # Script to load data from API
│   └── clean_utils.py       # Cleaning functions to import into notebooks
├── models/                  # Trained models, SHAP outputs
├── dashboards/                 # .pbix file or dashboard description
├── requirements.txt         # Dependencies
├── README.md                # This file
└── LICENSE                  # GNU GPL v3 License
```

## Data Source

**Source**: [CMS.gov Facility-Level Minimum Data Set Frequency](https://data.cms.gov/provider-data/dataset/4pq5-n9py)

**API Endpoint**: [CMS Data API](https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data)

This dataset includes:

* Resident characteristics (age, race, marital status)
* Health indicators (diagnoses, cognitive/mood status)
* Medications and treatments
* Functional and behavioral metrics

The project will use the API for live data ingestion and a small static CSV subset as a fallback or for development purposes.

## Workflow Summary

1. **Ingest Data**: Load raw CSV into a Pandas DataFrame or SQL database.
2. **Clean & Transform**: Handle missing values, encode categorical variables, standardize scales.
3. **Modeling**:

   * Cluster residents or predict risk factors.
   * Use SHAP for interpretability.
   * Store outputs for use in Power BI.
4. **Power BI Dashboard**:

   * Import aggregated and modeled data.
   * Design a dashboard with interactivity and clarity in mind.

## Dashboard Preview

> \[I will include a screenshot here of the Power BI dashboard once it is available. It will be uploaded to GitHub and linked using markdown.]

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

# Fetch initial data from CMS API
$ python scripts/fetch_data.py
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

**Joseph Chege Mungai**

Recent NYU Graduate | Math & CS | Python & Data Science Enthusiast

GitHub: [@JosephChege4](https://github.com/JosephChege4)
