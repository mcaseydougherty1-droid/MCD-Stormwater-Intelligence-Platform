import pandas as pd


def assign_owner_type(owner_name: str, hoa_flag: bool = False) -> str:
    name = str(owner_name).upper()

    if hoa_flag:
        return "HOA / Common Area"

    if any(term in name for term in ["ASSOCIATION", "HOMEOWNER", " HOA", "CONDO"]):
        return "HOA / Common Area"

    if any(term in name for term in ["LLC", "INC", "CORP", "COMPANY", "LP", "LLP", "PROPERTIES"]):
        return "Commercial Owner"

    if any(term in name for term in ["TOWNSHIP", "AUTHORITY", "SCHOOL", "CHURCH", "COUNTY"]):
        return "Institutional / Municipal"

    return "Residential / Other"


def enrich_owner_profiles(owner_registry: pd.DataFrame) -> pd.DataFrame:
    df = owner_registry.copy()

    df["Owner_Type"] = df.apply(
        lambda row: assign_owner_type(
            row.get("Owner_Name", ""),
            bool(row.get("HOA_Flag", False)),
        ),
        axis=1,
    )

    df["O&M_Flag"] = df["Verified_Document_Count"].fillna(0).astype(int) > 0

    return df