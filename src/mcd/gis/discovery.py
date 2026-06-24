from typing import Any

from mcd.gis.catalog import ArcGISLayer, ArcGISService
from mcd.gis.client import ArcGISClient


class ArcGISDiscovery:
    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip("/")
        self.client = ArcGISClient(self.server_url)

    def list_services(self) -> list[ArcGISService]:
        services: list[ArcGISService] = []

        response: dict[str, Any] = self.client.get(
            endpoint="services",
            params={"f": "json"},
        )

        for service in response.get("services", []):
            services.append(self._build_service(service))

        for folder in response.get("folders", []):
            folder_response: dict[str, Any] = self.client.get(
                endpoint=f"services/{folder}",
                params={"f": "json"},
            )

            for service in folder_response.get("services", []):
                services.append(
                    self._build_service(
                        service=service,
                        folder=folder,
                    )
                )

        return services

    def _build_service(
        self,
        service: dict[str, Any],
        folder: str | None = None,
    ) -> ArcGISService:
        name = service.get("name", "")
        service_type = service.get("type", "")

        if folder:
            clean_name = name.removeprefix(f"{folder}/")
            url = f"{self.server_url}/services/{folder}/{clean_name}/{service_type}"
        else:
            clean_name = name
            url = f"{self.server_url}/services/{clean_name}/{service_type}"

        return ArcGISService(
            name=clean_name,
            type=service_type,
            url=url,
        )

    def list_layers(self, service: ArcGISService) -> list[ArcGISLayer]:
        endpoint = service.url.replace(f"{self.server_url}/", "")

        response: dict[str, Any] = self.client.get(
            endpoint=endpoint,
            params={"f": "json"},
        )

        layers: list[ArcGISLayer] = []

        for layer in response.get("layers", []):
            layers.append(
                ArcGISLayer(
                    id=layer["id"],
                    name=layer["name"],
                    url=f"{service.url}/{layer['id']}",
                )
            )

        return layers