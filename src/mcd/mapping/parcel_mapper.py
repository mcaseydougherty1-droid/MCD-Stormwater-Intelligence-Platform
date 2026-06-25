import pandas as pd


def prepare_parcel_map_points(parcels: pd.DataFrame) -> pd.DataFrame:
    df = parcels.copy()

    if "Latitude" not in df.columns:
        df["Latitude"] = None

    if "Longitude" not in df.columns:
        df["Longitude"] = None

    return df.dropna(subset=["Latitude", "Longitude"], how="any")
