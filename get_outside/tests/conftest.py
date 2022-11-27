# from pytest_factoryboy import register
# from .factories import CategoryFactory

# # Register Approach

# register(CategoryFactory)
from .factories import CategoryFactory
import pytest

@pytest.fixture
def data():
    return CategoryFactory.create_batch(10)
