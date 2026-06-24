import pandas as pd


def build_scope_summary(account: pd.Series) -> str:
    bmp_count = int(account.get("BMP_Count", 0) or 0)
    owner = account.get("Owner_Name", account.get("Owner", "the property owner"))

    return (
        f"MCD Consulting will provide stormwater maintenance support for {owner}, "
        f"including review and field verification of approximately {bmp_count} BMP asset(s), "
        "vegetation management recommendations, inspection planning, and identification of "
        "maintenance needs tied to stormwater compliance obligations."
    )


def build_service_lines(account: pd.Series) -> list[str]:
    return [
        "Stormwater BMP field verification",
        "Vegetation and basin maintenance assessment",
        "O&M agreement and document review",
        "Maintenance priority recommendations",
        "Annual stormwater maintenance planning",
    ]
