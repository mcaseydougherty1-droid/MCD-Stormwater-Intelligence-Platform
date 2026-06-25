import pandas as pd


def add_activity_fields(opportunities: pd.DataFrame) -> pd.DataFrame:
    df = opportunities.copy()

    df["Assigned_Representative"] = "MCD Consulting"
    df["Last_Contact_Date"] = ""
    df["Next_Follow_Up_Date"] = ""
    df["Expected_Close_Date"] = ""
    df["Proposal_Status"] = "Not started"
    df["CRM_Notes"] = ""

    return df
