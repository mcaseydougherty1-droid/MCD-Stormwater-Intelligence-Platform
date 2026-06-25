from pydantic import BaseModel


class PropertyResponse(BaseModel):
    pin: str
    owner: str | None = None
    property_address: str | None = None
    municipality: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    bmp_count: int = 0
    estimated_total_annual_revenue: float = 0
    expected_value: float = 0
    hoa_flag: bool = False
    owner_type: str | None = None

    model_config = {
        "from_attributes": True
    }
