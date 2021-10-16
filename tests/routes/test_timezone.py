import pytest


@pytest.mark.parametrize(
    ["coordinates", "timezone"],
    [
        ((40.741895, -73.989308), "America/New_York"),
        ((50.8465573, 4.351697), "Europe/Brussels"),
    ],
)
def test_timezone(gopos, coordinates, timezone):
    assert gopos.get_timezone(*coordinates) == timezone
