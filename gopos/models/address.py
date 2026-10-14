import dataclasses

# Public interface.
__all__ = ["GoposAddressInfo", "GoposNormaliseResponse", "GoposResolveResponse"]


@dataclasses.dataclass
class GoposAddressInfo:
    """
    Structured fields of an address.
    """

    city: str = ""
    country: str = ""
    postal_code: str = ""
    state_or_province: str = ""
    street: str = ""
    street_number: str = ""
    unit: str = ""


@dataclasses.dataclass
class GoposNormaliseResponse:
    """
    Response of a request to the `GET /address/normalise` route.
    """

    normalised: list[str]
    query: str


@dataclasses.dataclass
class GoposResolveResponse:
    """
    Response of a request to the `GET /address/resolve` route.
    """

    address_info: GoposAddressInfo
    display_address: str
    query: str
    resolver: str
