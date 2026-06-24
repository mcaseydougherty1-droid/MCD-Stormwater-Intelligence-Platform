from dataclasses import dataclass


@dataclass
class ArcGISLayer:
    id: int
    name: str
    url: str


@dataclass
class ArcGISService:
    name: str
    type: str
    url: str