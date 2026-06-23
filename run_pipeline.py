import pandas as pd
from pathlib import Path
from src.mcd_platform.config import PARCEL_LAYER_URL, MUNICIPALITY, OUTPUT_EXCEL, INPUT_DIR, OUTPUT_DIR, MAX_RECORDS
from src.mcd_platform.arcgis import query_layer
from src.mcd_platform.classify import normalize_columns, classify_parcels, score_pipeline
from src.mcd_platform.export import export_workbook


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    print("Connecting to Butler County ArcGIS parcel layer...")
    raw = query_layer(PARCEL_LAYER_URL, max_records=MAX_RECORDS)
    raw.to_csv(OUTPUT_DIR / "raw_parcels.csv", index=False)
    print(f"Downloaded {len(raw)} parcel records.")

    parcels = normalize_columns(raw)
    # Filter municipality when the layer exposes a municipality field. If not, keep all records and let user filter in Excel.
    if parcels["Municipality"].str.strip().ne("").any():
        mask = parcels["Municipality"].str.contains("Adams", case=False, na=False)
        if mask.any():
            parcels = parcels[mask].copy()
    parcels = classify_parcels(parcels)
    pipeline = score_pipeline(parcels[parcels["Target_Flag"]].copy())

    docs_path = INPUT_DIR / "document_crosswalk.csv"
    docs = pd.read_csv(docs_path) if docs_path.exists() else pd.DataFrame(columns=["PIN", "OM_Agreement_Status", "OM_Document_Link", "SWM_Plan_Link", "Record_Drawings_Link", "Easement_Link", "Document_Notes"])

    inspections = pipeline[["PIN", "Owner", "Property_Address", "MCD_Target_Category", "Priority_Score", "Pipeline_Tier"]].copy()
    inspections["Inspection_Status"] = "Not Scheduled"
    inspections["Recommended_Frequency"] = inspections["Pipeline_Tier"].astype(str).map({"A": "Quarterly", "B": "Semiannual", "C": "Annual", "D": "As needed"})
    inspections["Next_Inspection_Date"] = ""
    inspections["Inspector"] = ""
    inspections["Notes"] = ""

    export_workbook(OUTPUT_EXCEL, parcels, pipeline, docs, inspections)
    print(f"Excel database created: {OUTPUT_EXCEL}")
    print("Next: run 'streamlit run app.py' to open the map/dashboard.")


if __name__ == "__main__":
    main()
