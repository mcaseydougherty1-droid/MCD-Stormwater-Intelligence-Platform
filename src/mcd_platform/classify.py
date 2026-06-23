import pandas as pd

KEYWORDS = {
    "HOA/Common Area": ["HOMEOWNER", "HOME OWNER", " HOA", "ASSOCIATION", "CONDOMINIUM", "CONDO", "COMMON", "OPEN SPACE"],
    "Commercial": ["LLC", "INC", "CORP", "COMPANY", "LP", "LLP", "LTD", "RETAIL", "PLAZA", "PROPERTIES", "REALTY"],
    "Institutional": ["SCHOOL", "CHURCH", "PARISH", "TOWNSHIP", "AUTHORITY", "COUNTY", "MUNICIPAL", "HOSPITAL", "UNIVERSITY"],
}


def first_existing(df: pd.DataFrame, candidates: list[str]) -> str | None:
    lower = {c.lower(): c for c in df.columns}
    for candidate in candidates:
        if candidate.lower() in lower:
            return lower[candidate.lower()]
    return None


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    pin = first_existing(df, ["PIN", "PARCEL", "PARCEL_ID", "PARID", "MAP_PAR_ID", "UPI", "OBJECTID"])
    owner = first_existing(df, ["OWNER", "OWNER1", "OWNER_NAME", "OWNERNME1", "NAME", "TAXPAYER"])
    site = first_existing(df, ["SITE_ADDR", "PROPERTY_ADDRESS", "ADDRESS", "LOCADDR", "SITUS", "PROPADDR"])
    muni = first_existing(df, ["MUNICIPALITY", "MUNI", "MUNICIPALI", "MUNICIPAL", "TWP"])
    acres = first_existing(df, ["ACRES", "Shape__Area", "Shape_Area", "GIS_ACRES"])
    use = first_existing(df, ["LAND_USE", "CLASS", "PROPERTY_CLASS", "USE", "LUC", "TYPE"])

    out = pd.DataFrame()
    out["PIN"] = df[pin].astype(str) if pin else df.index.astype(str)
    out["Owner"] = df[owner].astype(str) if owner else ""
    out["Property_Address"] = df[site].astype(str) if site else ""
    out["Municipality"] = df[muni].astype(str) if muni else ""
    out["Acres"] = pd.to_numeric(df[acres], errors="coerce") if acres else 0
    out["Land_Use"] = df[use].astype(str) if use else ""
    out["Latitude"] = pd.to_numeric(df.get("latitude", None), errors="coerce") if "latitude" in df else None
    out["Longitude"] = pd.to_numeric(df.get("longitude", None), errors="coerce") if "longitude" in df else None
    return out


def classify_parcels(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    blob = (df["Owner"].fillna("") + " " + df["Property_Address"].fillna("") + " " + df["Land_Use"].fillna("")).str.upper()
    categories = []
    for text in blob:
        cat = "Residential/Other"
        for label, words in KEYWORDS.items():
            if any(w in text for w in words):
                cat = label
                break
        categories.append(cat)
    df["MCD_Target_Category"] = categories
    df["Target_Flag"] = df["MCD_Target_Category"].ne("Residential/Other")
    df["Likely_BMP_Types"] = df["MCD_Target_Category"].map({
        "HOA/Common Area": "detention basin; retention pond; swale; outlet structure",
        "Commercial": "underground chambers; detention basin; inlet/outlet structures",
        "Institutional": "detention basin; rain garden; swales; outlet structures",
        "Residential/Other": "unknown",
    })
    df["Estimated_Maintenance_Need"] = df["MCD_Target_Category"].map({
        "HOA/Common Area": "High",
        "Commercial": "Medium-High",
        "Institutional": "Medium",
        "Residential/Other": "Low/Unknown",
    })
    return df


def score_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    score = df["Target_Flag"].astype(int) * 20
    score += df["MCD_Target_Category"].eq("HOA/Common Area").astype(int) * 20
    score += df["MCD_Target_Category"].eq("Commercial").astype(int) * 15
    score += df["MCD_Target_Category"].eq("Institutional").astype(int) * 10
    score += df["Acres"].fillna(0).clip(0, 20) * 2
    df["Priority_Score"] = score.round(0).astype(int)
    df["Pipeline_Tier"] = pd.cut(df["Priority_Score"], bins=[-1, 19, 39, 59, 999], labels=["D", "C", "B", "A"])
    df["Estimated_Annual_Revenue"] = df["Priority_Score"].apply(lambda s: 0 if s < 20 else 1500 + s * 75)
    df["Sales_Stage"] = "Research"
    df["Next_Action"] = "Verify O&M/SWM records and owner contact"
    return df.sort_values(["Priority_Score", "Owner"], ascending=[False, True])
