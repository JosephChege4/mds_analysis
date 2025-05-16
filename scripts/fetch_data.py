import requests as req
import pandas as pd


def fetch_cms_data(api_url: str, limit: int = 5000) -> pd.DataFrame:
    """
    Fetches data from the CMS API endpoint.

    Parameters:
        api_url (str): The URL to the CMS dataset API.
        limit (int): Number of records to fetch (CMS API allows pagination).

    Returns:
        pd.DataFrame: DataFrame containing the fetched data.
    """

    res = req.get(api_url, params={"limit": limit})
    res.raise_for_status()
    data = res.json()
    return pd.DataFrame(data)


if __name__ == "__main__":
    API_URL = "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data"
    df = fetch_cms_data(API_URL)
    df.to_csv("data/raw_mds_sample.csv", index=False)
    print(f"Fetched {len(df)} records and saved to data/raw_mds_cample.csv")
