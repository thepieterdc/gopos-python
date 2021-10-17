# gopos-python

![https://img.shields.io/pypi/v/gopos?style=flat-square](https://img.shields.io/pypi/v/gopos?style=flat-square)

Python bindings for gopos (https://github.com/thepieterdc/gopos).

## Installation
```shell
pip install gopos
```

## Usage

```python
from gopos import GoposClient

# Initialise a client.
client = GoposClient("http://gopos.local:8000")

# Parse the given address.
address = "Champ de Mars, 5 Av. Anatole France, 75007 Paris"
print(client.parse_address(address))

# Output:
# GoposAddress(
#    category=None, 
#    city='paris',
#    city_district=None,
#    country=None,
#    country_region=None,
#    entrance=None,
#    house=None,
#    house_number=None,
#    island=None,
#    level=None,
#    near=None,
#    po_box=None,
#    postcode='75007',
#    road='champ de mars 5 av. anatole france',
#    staircase=None,
#    state=None,
#    state_district=None,
#    suburb=None,
#    unit=None,
#    world_region=None)
```