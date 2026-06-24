import pandas as pd

from mcd.contacts.hoa_contacts import assign_hoa_contact_status
from mcd.contacts.management_companies import assign_management_company


CONTACT_COLUMNS = [
    "Owner_Name",
    "Owner_Type",
    "HOA_Flag",
    "Management_Company",
    "Primary_Contact",
    "Contact_Title",
    "Email",
    "Phone",
    "Website",
    "Mailing_Address",
    "BMP_Count",
    "Estimated_Total_Annual_Revenue",
    "Expected_Value",
    "Owner_Intelligence_Score",
    "Priority_Tier",
    "HOA_Contact_Status",
    "Outreach_Status",
    "Contact_Next_Action",
]


def build_contact_registry(owner_intelligence: pd.DataFrame) -> pd.DataFrame:
    df = owner_intelligence.copy()

    df["Management_Company"] = df.apply(assign_management_company, axis=1)
    df["HOA_Contact_Status"] = df.apply(assign_hoa_contact_status, axis=1)

    df["Primary_Contact"] = ""
    df["Contact_Title"] = ""
    df["Email"] = ""
    df["Phone"] = ""
    df["Website"] = ""
    df["Mailing_Address"] = ""

    available_columns = [column for column in CONTACT_COLUMNS if column in df.columns]

    return df[available_columns].copy()