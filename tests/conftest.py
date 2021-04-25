"""Store the classes and fixtures used throughout the tests."""

import pytest
from faker import Faker

from faker_optional import OptionalProvider


@pytest.fixture(scope="module")
def fake() -> Faker:
    """Configure the faker instance."""
    fixture = Faker()
    fixture.add_provider(OptionalProvider)
    return fixture
