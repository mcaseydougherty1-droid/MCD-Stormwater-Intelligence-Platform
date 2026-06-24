import pandas as pd


KNOWN_MANAGEMENT_COMPANY_TERMS = [
    "MANAGEMENT",
    "PROPERTY MANAGEMENT",
    "COMMUNITY MANAGEMENT",
    "REALTY",
    "ASSOCIATION MANAGEMENT",
]


def detect_management_company(owner_name: str) -> str:
    name = str(owner_name).upper()

    if any(term in name for term in KNOWN_MANAGEMENT_COMPANY_TERMS):
        return owner_name

    return ""


def assign_management_company(row: pd.Series) -> str:
    owner_name = str(row.get("Owner_Name", ""))

    detected = detect_management_company(owner_name)

    if detected:
        return detected

    return ""