# from pytest_factoryboy import register
# from .factories import CategoryFactory

# # Register Approach

# register(CategoryFactory)
from .factories import CategoryFactory
# , MappointFactory
import pytest

@pytest.fixture
def data():
    return CategoryFactory.create_batch(10)

# @pytest.fixture
# def data():
#     return MappointFactory.create_batch(10)
