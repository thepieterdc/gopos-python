ADDRESS = "Apple 10955 N Tantau Ave, Cupertino, CA 95014, United States"


def test_normalise_address(gopos):
    normalised = gopos.normalise_address(ADDRESS)

    assert normalised
    assert any("north tantau avenue" in variant for variant in normalised)


def test_resolve_address(gopos):
    resolved = gopos.resolve_address(ADDRESS)

    assert resolved.query == ADDRESS
    assert resolved.resolver == "libpostal"
    assert resolved.display_address
    assert resolved.address_info.city == "cupertino"
    assert resolved.address_info.country == "united states"
    assert resolved.address_info.state_or_province == "california"
    assert resolved.address_info.street == "north tantau avenue"
    assert resolved.address_info.street_number == "10955"
