import requests
import pandas as pd


def query_layer(layer_url: str, where: str = "1=1", out_fields: str = "*", result_record_count: int = 2000, max_records: int = 50000) -> pd.DataFrame:
    """Query an ArcGIS REST layer with pagination and return attributes as a DataFrame."""
    rows = []
    offset = 0
    while offset < max_records:
        params = {
            "f": "json",
            "where": where,
            "outFields": out_fields,
            "returnGeometry": "true",
            "outSR": "4326",
            "resultOffset": offset,
            "resultRecordCount": result_record_count,
        }
        r = requests.get(f"{layer_url}/query", params=params, timeout=60)
        r.raise_for_status()
        data = r.json()
        if "error" in data:
            raise RuntimeError(data["error"])
        features = data.get("features", [])
        if not features:
            break
        for feature in features:
            attrs = feature.get("attributes", {}) or {}
            geom = feature.get("geometry", {}) or {}
            # Store a simple representative coordinate when available.
            if "x" in geom and "y" in geom:
                attrs["longitude"] = geom["x"]
                attrs["latitude"] = geom["y"]
            elif "rings" in geom and geom["rings"]:
                pts = geom["rings"][0]
                if pts:
                    attrs["longitude"] = sum(p[0] for p in pts) / len(pts)
                    attrs["latitude"] = sum(p[1] for p in pts) / len(pts)
            rows.append(attrs)
        if not data.get("exceededTransferLimit") and len(features) < result_record_count:
            break
        offset += result_record_count
    return pd.DataFrame(rows)


def get_layer_fields(layer_url: str) -> list[str]:
    r = requests.get(layer_url, params={"f": "json"}, timeout=60)
    r.raise_for_status()
    data = r.json()
    return [f.get("name") for f in data.get("fields", [])]
