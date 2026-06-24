from dataclasses import dataclass


@dataclass
class Parcel:
    parcel_id: str
    owner: str
    property_address: str
    municipality: str
    acres: float | None = None
    land_use: str | None = None
    latitude: float | None = None
    longitude: float | None = None


@dataclass
class Opportunity:
    parcel_id: str
    category: str
    priority_score: int
    pipeline_tier: str
    estimated_annual_revenue: float