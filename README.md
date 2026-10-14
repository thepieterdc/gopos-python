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

# Resolve the given address.
address = "Champ de Mars, 5 Av. Anatole France, 75007 Paris"
print(client.resolve_address(address, country="fr"))

# Normalise the given address into its possible expansions.
print(client.normalise_address(address))
```