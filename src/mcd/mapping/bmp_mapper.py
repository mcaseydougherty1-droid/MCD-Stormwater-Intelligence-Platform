import pandas as pd


def prepare_bmp_map_points(bmp_inventory: pd.DataFrame) -> pd.DataFrame:
    df = bmp_inventory.copy()

    if "Latitude" not in df.columns:
        df["Latitude"] = None

    if "Longitude" not in df.columns:
        df["Longitude"] = None

    return df.dropna(subset=["Latitude", "Longitude"], how="any")
