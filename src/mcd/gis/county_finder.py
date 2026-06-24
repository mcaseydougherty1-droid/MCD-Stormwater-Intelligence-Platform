from mcd.gis.classifier import LayerCategory, LayerClassifier
from mcd.gis.discovery import ArcGISDiscovery


class CountyLayerFinder:
    def __init__(self, server_url: str):
        self.discovery = ArcGISDiscovery(server_url)

    def find_relevant_layers(self) -> list[dict[str, str]]:
        results: list[dict[str, str]] = []

        services = self.discovery.list_services()

        for service in services:
            layers = self.discovery.list_layers(service)

            for layer in layers:
                category = LayerClassifier.classify(layer.name)

                if category != LayerCategory.UNKNOWN:
                    results.append(
                        {
                            "category": category.value,
                            "service": service.name,
                            "service_type": service.type,
                            "layer": layer.name,
                            "url": layer.url,
                        }
                    )

        return results