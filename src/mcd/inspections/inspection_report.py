import pandas as pd


def build_compliance_calendar(schedule: pd.DataFrame) -> pd.DataFrame:
    df = schedule.copy()

    df["Compliance_Item"] = "Stormwater BMP inspection"
    df["Compliance_Status"] = "Scheduled"
    df["Regulatory_Risk"] = df["Inspection_Frequency"].map(
        {
            "Semiannual": "High",
            "Annual": "Medium",
        }
    ).fillna("Medium")

    df["Client_Report_Status"] = "Not generated"

    return df[
        [
            "BMP_ID",
            "Owner",
            "PIN",
            "Property_Address",
            "BMP_Type",
            "Compliance_Item",
            "Next_Inspection_Date",
            "Compliance_Status",
            "Regulatory_Risk",
            "Client_Report_Status",
        ]
    ]
