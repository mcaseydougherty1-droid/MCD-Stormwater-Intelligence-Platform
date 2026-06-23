from enum import Enum


class LayerCategory(str, Enum):
    PARCEL = "parcel"
    STORMWATER = "stormwater"
    BMP = "bmp"
    HYDROLOGY = "hydrology"
    BOUNDARY = "boundary"
    TRANSPORTATION = "transportation"
    IMAGERY = "imagery"
    FLOODPLAIN = "floodplain"
    ZONING = "zoning"
    UNKNOWN = "unknown"
    from typing import Iterable


class LayerClassifier:

    KEYWORDS = {
        LayerCategory.PARCEL: [
            "parcel",
            "tax",
            "property",
            "ownership",
            "assessment",
        ],
        LayerCategory.STORMWATER: [
            "storm",
            "drain",
            "sewer",
            "catch basin",
            "inlet",
            "outfall",
        ],
        LayerCategory.BMP: [
            "bmp",
            "detention",
            "retention",
            "basin",
            "pond",
            "swm",
            "stormwater facility",
        ],
        LayerCategory.HYDROLOGY: [
            "stream",
            "creek",
            "river",
            "water",
            "hydrology",
        ],
        LayerCategory.BOUNDARY: [
            "municipal",
            "boundary",
            "township",
            "borough",
            "county",
        ],
        LayerCategory.TRANSPORTATION: [
            "road",
            "street",
            "highway",
            "transportation",
        ],
        LayerCategory.IMAGERY: [
            "imagery",
            "ortho",
            "aerial",
        ],
        LayerCategory.FLOODPLAIN: [
            "flood",
            "fema",
            "100 year",
        ],
        LayerCategory.ZONING: [
            "zoning",
            "land use",
        ],
    }
    @classmethod
    def classify(cls, layer_name: str) -> LayerCategory:
        """
        Classify a GIS layer by matching keywords in its name.
        """

        name = layer_name.lower()

        for category, keywords in cls.KEYWORDS.items():
            for keyword in keywords:
                if keyword in name:
                    return category

        return LayerCategory.UNKNOWN