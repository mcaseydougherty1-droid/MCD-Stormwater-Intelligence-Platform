from typing import Any

from .client import ArcGISClient
from .catalog import ArcGISLayer, ArcGISService


class ArcGISDiscovery:
    """
    Discovers ArcGIS services and layers from an ArcGIS Server REST endpoint.
    """

    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip("/")
        self.client = ArcGISClient(self.server_url)

    def list_services(self) -> list[ArcGISService]:
        """
        List ArcGIS services available from the server.
        """

        response: dict[str, Any] = self.client.get(
            endpoint="services",
            params={"f": "json"},
        )

        services = []

        for service in response.get("services", []):
            name = service.get("name", "")
            service_type = service.get("type", "")

            services.append(
                ArcGISService(
                    name=name,
                    type=service_type,
                    url=f"{self.server_url}/services/{name}/{service_type}",
                )
            )

        return services
    def list_layers(
        self,
        service: ArcGISService,
    ) -> list[ArcGISLayer]:
        """
        Discover every layer inside a MapServer.
        """

        response = self.client.get(
            endpoint=f"services/{service.name}/{service.type}",
            params={"f": "json"},
        )

        layers = []

        for layer in response.get("layers", []):

            layers.append(
                ArcGISLayer(
                    id=layer["id"],
                    name=layer["name"],
                    url=f"{service.url}/{layer['id']}",
                )
            )

        return layers