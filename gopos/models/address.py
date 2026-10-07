import dataclasses

# Public interface.
__all__ = ["GoposAddress"]


@dataclasses.dataclass
class GoposAddress:
    """
    Response of a request to the `GET /address/parse` route.

    Definition of the fields is available at:
    https://github.com/openvenues/libpostal#parser-labels.
    """

    category: str | None = None
    city: str | None = None
    city_district: str | None = None
    country: str | None = None
    country_region: str | None = None
    entrance: str | None = None
    house: str | None = None
    house_number: str | None = None
    island: str | None = None
    level: str | None = None
    near: str | None = None
    po_box: str | None = None
    postcode: str | None = None
    road: str | None = None
    staircase: str | None = None
    state: str | None = None
    state_district: str | None = None
    suburb: str | None = None
    unit: str | None = None
    world_region: str | None = None
