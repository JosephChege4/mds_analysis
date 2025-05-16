import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes column names to lowercase and underscores.
    """
    df.columns(
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
        .str.replace("-", "_")
    )
    return df


def drop_empty_columns(df: pd.DataFrame, threshold: float = 0.9) -> pd.DataFrame:
    """
    Drops columns with more than `threshold` proportion of missing values.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        threshold (float): Proportion of missing values to tolerate.

    Returns:
        pd.DataFrame
    """
    return df.loc[:, df.isnull().mean() < threshold]


def encode_categoricals(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """One-hot encodes the given categorical columns."""
    return pd.get_dummies(df, columns=columns, drop_first=True)


def normalize_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Min-max scales the specified numeric columns."""
    for col in columns:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)
    return df
