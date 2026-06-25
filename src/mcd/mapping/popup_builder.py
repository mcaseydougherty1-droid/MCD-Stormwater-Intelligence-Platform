import pandas as pd


def build_popup(row: pd.Series) -> str:
    owner = row.get("Owner", "")
    bmp_type = row.get("BMP_Type", "")
    address = row.get("Property_Address", "")
    pin = row.get("PIN", "")
    revenue = row.get("Estimated_Annual_Cost", 0)
    confidence = row.get("Confidence_Score", "")

    return f"""
    <b>Owner:</b> {owner}<br>
    <b>PIN:</b> {pin}<br>
    <b>Address:</b> {address}<br>
    <b>BMP Type:</b> {bmp_type}<br>
    <b>Estimated Annual Cost:</b> ${revenue:,.0f}<br>
    <b>Confidence Score:</b> {confidence}<br>
    """
