def test_parse_address(gopos):
    address = gopos.parse_address(
        "Apple 10955 N Tantau Ave, Cupertino, CA 95014, United States")

    assert address.city == "cupertino"
    assert address.country == "united states"
    assert address.house == "apple"
    assert address.house_number == "10955"
    assert address.postcode == "95014"
    assert address.road == "n tantau ave"
    assert address.state == "ca"
