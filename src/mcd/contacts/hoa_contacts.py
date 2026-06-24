import pandas as pd


def is_likely_hoa(owner_type: str, owner_name: str) -> bool:
    text = f"{owner_type} {owner_name}".upper()

    return any(
        term in text
        for term in [
            "HOA",
            "HOMEOWNER",
            "HOME OWNER",
            "ASSOCIATION",
            "CONDOMINIUM",
            "CONDO",
            "COMMON AREA",
        ]
    )


def assign_hoa_contact_status(row: pd.Series) -> str:
    if is_likely_hoa(row.get("Owner_Type", ""), row.get("Owner_Name", "")):
        return "Needs HOA board or management company lookup"

    return "Not HOA-specific"