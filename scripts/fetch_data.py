import requests
import pandas as pd
import time
import os
from typing import Dict, Optional
from datetime import datetime

# Directory setup
RAW_DATA_DIR = "data/raw"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

# CMS API endpoints
DATASETS: Dict[str, str] = {
    # Final 2 JSON-only datasets
    "facility_level_mds_frequency": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data",
    "minimum_data_set_frequency": "https://data.cms.gov/data-api/v1/dataset/4b50bbe6-a496-4eda-b03b-5f835937f81b/data",
    # 17 datasets from provider portal (JSON via /datastore/query/)
    "provider_information": "https://data.cms.gov/provider-data/api/1/datastore/query/4pq5-n9py",
    "mds_quality_measures": "https://data.cms.gov/provider-data/api/1/datastore/query/qrzv-wzg8",
    "penalties": "https://data.cms.gov/provider-data/api/1/datastore/query/cg87-xh25",
    "state_level_health_inspection_cut_points": "https://data.cms.gov/provider-data/api/1/datastore/query/g6i4-kqyf",
    "fire_safety_deficiencies": "https://data.cms.gov/provider-data/api/1/datastore/query/vqhv-57b6",
    "medicare_claims_quality_measures": "https://data.cms.gov/provider-data/api/1/datastore/query/9wzi-peqs",
    "inspection_dates": "https://data.cms.gov/provider-data/api/1/datastore/query/wqib-ffaw",
    "survey_summary": "https://data.cms.gov/provider-data/api/1/datastore/query/ck7a-9ke6",
    "state_us_averages": "https://data.cms.gov/provider-data/api/1/datastore/query/b27b-2uc7",
    "ownership": "https://data.cms.gov/provider-data/api/1/datastore/query/qrfu-jxw5",
    "fy2025_snf_vbp_facility": "https://data.cms.gov/provider-data/api/1/datastore/query/gfak-4jue",
    "fy2025_snf_vbp_aggregate": "https://data.cms.gov/provider-data/api/1/datastore/query/mv7z-s9i4",
    "health_deficiencies": "https://data.cms.gov/provider-data/api/1/datastore/query/94xx-f87h",
    "nursing_home_data_collection_intervals": "https://data.cms.gov/provider-data/api/1/datastore/query/2utd-q6zu",
    "snf_qrp_national": "https://data.cms.gov/provider-data/api/1/datastore/query/28km-nzmh",
    "snf_qrp_swing_beds": "https://data.cms.gov/provider-data/api/1/datastore/query/6ni9-j8pf",
    "snf_qrp_provider": "https://data.cms.gov/provider-data/api/1/datastore/query/jbvm-jnvh",
}


def fetch_cms_data(api_url: str, limit: int = 5000, max_records=5000) -> pd.DataFrame:
    """
    Fetches paginated data from the CMS API.

    Parameters:
        api_url (str): CMS API endpoint.
        limit (int): Records per request.
        max_records (int): Optional cap on total records.

    Returns:
        pd.DataFrame: All combined data.
    """
    all_data = []
    offset = 0

    while True:
        params = {"limit": limit, "offset": offset}
        response = requests.get(api_url, params=params, timeout=15)
        response.raise_for_status()
        batch = response.json()

        if not batch:
            break

        all_data.extend(batch)
        offset += limit

        if max_records and len(all_data) >= max_records:
            break

    return pd.DataFrame(all_data)


def save_dataset(name: str, df: pd.DataFrame, subfolder: Optional[str] = None):
    """
    Saves a DataFrame as a CSV file to either 'data/raw' or custom location.

    Parameters:
        name (str): Base name of the file.
        df (pd.DataFrame): Data to write.
        subfolder (str): Folder to save into.
    """
    if subfolder is None:
        subfolder = RAW_DATA_DIR
    os.makedirs(subfolder, exist_ok=True)
    filepath = os.path.join(subfolder, f"{name}.csv")
    df.to_csv(filepath, index=False)
    print(f"Saved '{name}' ({len(df)} rows) to: {filepath}")


if __name__ == "__main__":
    print(f"[{datetime.now()}] Starting CMS data fetch...")

    for name, url in DATASETS.items():
        try:
            print(f"\nFetching dataset: {name}")
            df = fetch_cms_data(url)
            save_dataset(name, df)
            time.sleep(2)
        except Exception as e:
            print(f"Error fetching '{name}': {e}")

    print(f"\n[{datetime.now()}] Fetch complete.")
