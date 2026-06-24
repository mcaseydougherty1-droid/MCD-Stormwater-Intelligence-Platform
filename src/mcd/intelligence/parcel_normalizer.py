import pandas as pd


def first_existing(df: pd.DataFrame, candidates: list[str]) -> str | None:
    lower = {column.lower(): column for column in df.columns}

    for candidate in candidates:
        if candidate.lower() in lower:
            return lower[candidate.lower()]

    return None


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    pin = first_existing(df, ["PIN", "PARCEL", "PARCEL_ID", "PARID", "MAP_PAR_ID", "UPI", "OBJECTID"])
    owner = first_existing(df, ["OWNER", "OWNER1", "OWNER_NAME", "OWNERNME1", "NAME", "TAXPAYER"])
    site = first_existing(df, ["PhysicalAddress", "SITE_ADDR", "PROPERTY_ADDRESS", "ADDRESS", "LOCADDR", "SITUS", "PROPADDR"])
    muni = first_existing(df, ["MunicipalityDescription", "MUNICIPALITY", "MUNI", "MUNICIPALI", "MUNICIPAL", "TWP"])
    acres = first_existing(df, ["ACRES", "Shape__Area", "Shape_Area", "GIS_ACRES"])
    land_use = first_existing(df, ["LandUseCode", "LAND_USE", "CLASS", "PROPERTY_CLASS", "USE", "LUC", "TYPE"])

    out = pd.DataFrame()
    out["PIN"] = df[pin].astype(str) if pin else df.index.astype(str)
    out["Owner"] = df[owner].astype(str) if owner else ""
    out["Property_Address"] = df[site].astype(str) if site else ""
    out["Municipality"] = df[muni].astype(str) if muni else ""
    out["Acres"] = pd.to_numeric(df[acres], errors="coerce") if acres else 0
    out["Land_Use"] = df[land_use].astype(str) if land_use else ""
    out["Latitude"] = pd.to_numeric(df["latitude"], errors="coerce") if "latitude" in df else None
    out["Longitude"] = pd.to_numeric(df["longitude"], errors="coerce") if "longitude" in df else None

    return out