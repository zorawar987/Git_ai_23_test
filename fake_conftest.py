import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()
