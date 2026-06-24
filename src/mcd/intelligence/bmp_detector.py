import pandas as pd


BMP_RULES = {
    "HOA/Common Area": {
        "likely_bmp": True,
        "confidence": "High",
        "opportunity_type": "HOA stormwater basin / common-area BMP maintenance",
        "estimated_contract": 4500,
    },
    "Commercial": {
        "likely_bmp": True,
        "confidence": "Medium-High",
        "opportunity_type": "Commercial stormwater facility maintenance",
        "estimated_contract": 3500,
    },
    "Institutional": {
        "likely_bmp": True,
        "confidence": "Medium",
        "opportunity_type": "Institutional stormwater maintenance / inspection",
        "estimated_contract": 2500,
    },
    "Residential/Other": {
        "likely_bmp": False,
        "confidence": "Low",
        "opportunity_type": "Low-confidence residential parcel",
        "estimated_contract": 0,
    },
}


def detect_likely_bmps(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Likely_BMP_Present"] = df["MCD_Target_Category"].map(
        lambda category: BMP_RULES.get(category, BMP_RULES["Residential/Other"])["likely_bmp"]
    )

    df["BMP_Confidence"] = df["MCD_Target_Category"].map(
        lambda category: BMP_RULES.get(category, BMP_RULES["Residential/Other"])["confidence"]
    )

    df["Opportunity_Type"] = df["MCD_Target_Category"].map(
        lambda category: BMP_RULES.get(category, BMP_RULES["Residential/Other"])["opportunity_type"]
    )

    df["Estimated_Annual_Contract"] = df["MCD_Target_Category"].map(
        lambda category: BMP_RULES.get(category, BMP_RULES["Residential/Other"])["estimated_contract"]
    )

    return df