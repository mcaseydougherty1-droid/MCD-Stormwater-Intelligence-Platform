from enum import Enum


class DocumentType(str, Enum):
    OM_AGREEMENT = "O&M Agreement"
    SWM_PLAN = "Stormwater Management Plan"
    EASEMENT = "Stormwater Easement"
    AS_BUILT = "Record Drawing / As-Built"
    INSPECTION = "Inspection Report"
    UNKNOWN = "Unknown"