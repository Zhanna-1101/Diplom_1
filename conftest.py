import pytest
from unittest.mock import Mock
from data import TestData as td


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = td.bun_name
    mock_bun.get_price.return_value = td.bun_price
    return mock_bun


@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_type.return_value = td.sauce
    mock_sauce.get_name.return_value = td.sauce_name
    mock_sauce.get_price.return_value = td.sauce_price
    return mock_sauce


@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_type.return_value = td.filling
    mock_filling.get_name.return_value = td.filling_name
    mock_filling.get_price.return_value = td.filling_price
    return mock_filling
