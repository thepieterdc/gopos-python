import pytest

from gopos import GoposClient


@pytest.fixture(scope="session")
def gopos():
    yield GoposClient("http://localhost:8000")
