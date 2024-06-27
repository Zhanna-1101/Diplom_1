import pytest
from praktikum.ingredient import Ingredient
from data import TestData as td


@pytest.mark.parametrize('type, name, price', [[td.sauce, td.sauce_name, td.sauce_price],
                                               [td.filling, td.filling_name, td.filling_price]])
class TestIngredients:

    def test_get_type_ingredient_successfull(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type

    def test_get_name_ingredient_successfull(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    def test_get_price_ingredient_successfull(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price
