import pandas as pd


KEYWORDS = {
    "HOA/Common Area": [
        "HOMEOWNER",
        "HOME OWNER",
        " HOA",
        "ASSOCIATION",
        "CONDOMINIUM",
        "CONDO",
        "COMMON",
        "OPEN SPACE",
    ],
    "Commercial": [
        "LLC",
        "INC",
        "CORP",
        "COMPANY",
        "LP",
        "LLP",
        "LTD",
        "RETAIL",
        "PLAZA",
        "PROPERTIES",
        "REALTY",
    ],
    "Institutional": [
        "SCHOOL",
        "CHURCH",
        "PARISH",
        "TOWNSHIP",
        "AUTHORITY",
        "COUNTY",
        "MUNICIPAL",
        "HOSPITAL",
        "UNIVERSITY",
    ],
}


def classify_parcels(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    blob = (
        df["Owner"].fillna("")
        + " "
        + df["Property_Address"].fillna("")
        + " "
        + df["Land_Use"].fillna("")
    ).str.upper()

    categories = []

    for text in blob:
        category = "Residential/Other"

        for label, words in KEYWORDS.items():
            if any(word in text for word in words):
                category = label
                break

        categories.append(category)

    df["MCD_Target_Category"] = categories
    df["Target_Flag"] = df["MCD_Target_Category"].ne("Residential/Other")

    df["Likely_BMP_Types"] = df["MCD_Target_Category"].map(
        {
            "HOA/Common Area": "detention basin; retention pond; swale; outlet structure",
            "Commercial": "underground chambers; detention basin; inlet/outlet structures",
            "Institutional": "detention basin; rain garden; swales; outlet structures",
            "Residential/Other": "unknown",
        }
    )

    df["Estimated_Maintenance_Need"] = df["MCD_Target_Category"].map(
        {
            "HOA/Common Area": "High",
            "Commercial": "Medium-High",
            "Institutional": "Medium",
            "Residential/Other": "Low/Unknown",
        }
    )

    return df