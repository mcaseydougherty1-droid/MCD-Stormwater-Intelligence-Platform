from typing import Any

from .client import ArcGISClient
class ArcGISPaginator:
    """
    Retrieves every feature from an ArcGIS REST layer by
    automatically requesting all pages.
    """

    def __init__(self, client: ArcGISClient):
        self.client = client

    def get_total_count(self, layer_endpoint: str, where: str = "1=1") -> int:
        """
        Return the total number of records available from an ArcGIS layer.
        """

        params = {
            "where": where,
            "returnCountOnly": "true",
            "f": "json",
        }

        response = self.client.get(
            endpoint=f"{layer_endpoint.rstrip('/')}/query",
            params=params,
        )

        return int(response.get("count", 0))
    
    def fetch_page(
        self,
        layer_endpoint: str,
        offset: int,
        page_size: int,
        where: str = "1=1",
        out_fields: str = "*",
        return_geometry: bool = True,
    ) -> list[dict[str, Any]]:
        """
        Fetch one page of features from an ArcGIS layer.
        """

        params = {
            "where": where,
            "outFields": out_fields,
            "returnGeometry": str(return_geometry).lower(),
            "f": "json",
            "resultOffset": offset,
            "resultRecordCount": page_size,
        }

        response = self.client.get(
            endpoint=f"{layer_endpoint.rstrip('/')}/query",
            params=params,
        )

        return response.get("features", [])
    
    def fetch_all(
        self,
        layer_endpoint: str,
        where: str = "1=1",
        out_fields: str = "*",
        return_geometry: bool = True,
        page_size: int = 2000,
    ) -> list[dict[str, Any]]:
        """
        Fetch every available feature from an ArcGIS layer.
        """

        total_count = self.get_total_count(
            layer_endpoint=layer_endpoint,
            where=where,
        )

        all_features: list[dict[str, Any]] = []

        for offset in range(0, total_count, page_size):
            page = self.fetch_page(
                layer_endpoint=layer_endpoint,
                offset=offset,
                page_size=page_size,
                where=where,
                out_fields=out_fields,
                return_geometry=return_geometry,
            )

            all_features.extend(page)

            print(f"Downloaded {len(all_features)} of {total_count} features")

        return all_features