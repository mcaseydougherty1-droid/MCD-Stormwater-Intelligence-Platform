from datetime import date, timedelta

import pandas as pd


def assign_inspection_frequency(bmp_type: str) -> str:
    text = str(bmp_type).lower()

    if "underground" in text:
        return "Semiannual"

    if "detention" in text or "retention" in text:
        return "Annual"

    if "swale" in text or "rain garden" in text:
        return "Annual"

    return "Annual"


def next_inspection_date(frequency: str) -> str:
    today = date.today()

    if frequency == "Semiannual":
        return (today + timedelta(days=180)).isoformat()

    return (today + timedelta(days=365)).isoformat()


def build_inspection_schedule(bmp_inventory: pd.DataFrame) -> pd.DataFrame:
    df = bmp_inventory.copy()

    df["Inspection_Frequency"] = df["BMP_Type"].apply(assign_inspection_frequency)
    df["Next_Inspection_Date"] = df["Inspection_Frequency"].apply(next_inspection_date)
    df["Assigned_To"] = "Unassigned"
    df["Inspection_Status"] = "Scheduled"

    return df[
        [
            "BMP_ID",
            "Owner",
            "PIN",
            "Property_Address",
            "BMP_Type",
            "Inspection_Frequency",
            "Next_Inspection_Date",
            "Assigned_To",
            "Inspection_Status",
        ]
    ]
