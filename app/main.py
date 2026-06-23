import pandas as pd
import streamlit as st
from pathlib import Path
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="MCD Stormwater Intelligence Platform", layout="wide")
st.title("MCD Stormwater Intelligence Platform")

excel_path = Path("output/MCD_Stormwater_Intelligence_Platform.xlsx")
if not excel_path.exists():
    st.warning("Run `python run_pipeline.py` first to create the database.")
    st.stop()

pipeline = pd.read_excel(excel_path, sheet_name="Ranked Sales Pipeline")
parcels = pd.read_excel(excel_path, sheet_name="Master Inventory")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Parcels", len(parcels))
c2.metric("Target Prospects", len(pipeline))
c3.metric("A-Tier Prospects", int((pipeline["Pipeline_Tier"].astype(str)=="A").sum()))
c4.metric("Estimated Pipeline", f"${pipeline['Estimated_Annual_Revenue'].sum():,.0f}")

st.subheader("Ranked Sales Pipeline")
st.dataframe(pipeline, use_container_width=True)

st.subheader("Interactive Parcel Map")
map_df = pipeline.dropna(subset=["Latitude", "Longitude"]) if {"Latitude", "Longitude"}.issubset(pipeline.columns) else pd.DataFrame()
if map_df.empty:
    st.info("No coordinates were available from the parcel query. The Excel pipeline is still available.")
else:
    m = folium.Map(location=[map_df["Latitude"].mean(), map_df["Longitude"].mean()], zoom_start=12)
    for _, r in map_df.iterrows():
        folium.Marker(
            [r["Latitude"], r["Longitude"]],
            tooltip=f"{r.get('Owner','')} | Score {r.get('Priority_Score','')}",
            popup=f"<b>{r.get('Owner','')}</b><br>{r.get('Property_Address','')}<br>{r.get('MCD_Target_Category','')}<br>Score: {r.get('Priority_Score','')}",
        ).add_to(m)
    st_folium(m, width=1200, height=650)
