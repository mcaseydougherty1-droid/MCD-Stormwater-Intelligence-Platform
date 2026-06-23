import requests


class ArcGISClient:
    def __init__(self, layer_url: str, page_size: int = 2000):
        self.layer_url = layer_url.rstrip("/")
        self.page_size = page_size

    def get_record_count(self, where: str = "1=1") -> int:
        params = {
            "where": where,
            "returnCountOnly": "true",
            "f": "json",
        }
        response = requests.get(f"{self.layer_url}/query", params=params, timeout=60)
        response.raise_for_status()
        return response.json()["count"]

    def fetch_features(self, where: str = "1=1", out_fields: str = "*") -> list[dict]:
        total = self.get_record_count(where)
        features = []

        for offset in range(0, total, self.page_size):
            params = {
                "where": where,
                "outFields": out_fields,
                "returnGeometry": "true",
                "f": "json",
                "resultOffset": offset,
                "resultRecordCount": self.page_size,
            }

            response = requests.get(f"{self.layer_url}/query", params=params, timeout=120)
            response.raise_for_status()

            data = response.json()
            batch = data.get("features", [])
            features.extend(batch)

            print(f"Downloaded {len(features)} of {total} records")

        return features