import pandas as pd


def summarize_document_registry(registry: pd.DataFrame) -> pd.DataFrame:
    summary = registry.copy()

    summary["Has_OM_Agreement"] = summary["Document_Type"].str.contains(
        "O&M|Operation|Maintenance",
        case=False,
        na=False,
    )

    summary["Has_SWM_Plan"] = summary["Document_Type"].str.contains(
        "SWM|Stormwater Management Plan",
        case=False,
        na=False,
    )

    summary["Has_Easement"] = summary["Document_Type"].str.contains(
        "Easement",
        case=False,
        na=False,
    )

    return summary