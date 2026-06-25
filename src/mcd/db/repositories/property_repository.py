from sqlalchemy.orm import Session

from mcd.db.models.property import Property


def get_property_by_pin(session: Session, pin: str) -> Property | None:
    return session.query(Property).filter(Property.pin == pin).one_or_none()


def upsert_property(
    session: Session,
    *,
    pin: str,
    owner: str | None = None,
    property_address: str | None = None,
    municipality: str | None = None,
    latitude: float | None = None,
    longitude: float | None = None,
    bmp_count: int = 0,
    estimated_total_annual_revenue: float = 0,
    expected_value: float = 0,
    hoa_flag: bool = False,
    owner_type: str | None = None,
) -> Property:
    record = get_property_by_pin(session, pin)

    if record is None:
        record = Property(pin=pin)
        session.add(record)

    record.owner = owner
    record.property_address = property_address
    record.municipality = municipality
    record.latitude = latitude
    record.longitude = longitude
    record.bmp_count = bmp_count
    record.estimated_total_annual_revenue = estimated_total_annual_revenue
    record.expected_value = expected_value
    record.hoa_flag = hoa_flag
    record.owner_type = owner_type

    return record
