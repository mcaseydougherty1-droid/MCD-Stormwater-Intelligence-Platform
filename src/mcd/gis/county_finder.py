from .classifier import LayerClassifier, LayerCategory
from .discovery import ArcGISDiscovery


class CountyLayerFinder:
    """
    Finds stormwater-related GIS layers for a county.
    """

    def __init__(self, server_url: str):
        self.discovery = ArcGISDiscovery(server_url)

    def find_stormwater_layers(self):
        results = []

        services = self.discovery.list_services()

        for service in services:
            layers = self.discovery.list_layers(service)

            for layer in layers:
                category = LayerClassifier.classify(layer.name)

                if category != LayerCategory.UNKNOWN:
                    results.append(
                        {
                            "category": category.value,
                            "layer": layer.name,
                            "url": layer.url,
                        }
                    )

        return results