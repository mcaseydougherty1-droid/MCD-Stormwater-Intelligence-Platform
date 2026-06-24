import pandas as pd


def estimate_mowing_revenue(row: pd.Series) -> float:
    bmp_count = float(row.get("BMP_Count", 0) or 0)
    return bmp_count * 1800


def estimate_inspection_revenue(row: pd.Series) -> float:
    bmp_count = float(row.get("BMP_Count", 0) or 0)
    return bmp_count * 750


def estimate_dredging_allowance(row: pd.Series) -> float:
    bmp_count = float(row.get("BMP_Count", 0) or 0)
    return bmp_count * 500


def estimate_repair_allowance(row: pd.Series) -> float:
    bmp_count = float(row.get("BMP_Count", 0) or 0)
    return bmp_count * 350