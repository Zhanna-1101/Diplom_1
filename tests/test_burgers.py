import pytest
from praktikum.burger import Burger
from data import TestData as td


class TestBurgers:

    def test_set_buns_for_burger_successfull(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @pytest.mark.parametrize('mock_ingredient', ([td.sauce, td.sauce_name, td.sauce_price],
                                                 [td.filling, td.filling_name, td.filling_price]))
    def test_add_ingredient_in_burger_successfull(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient] and len(burger.ingredients) == 1

    def test_remove_ingredient_in_burger_successfull(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)

        assert mock_sauce not in burger.ingredients and len(burger.ingredients) == 1

    def test_move_ingredient_in_burger_successfull(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce
        assert len(burger.ingredients) == 2

    def test_get_price_burger_successfull(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == td.burger_cost

    def test_get_receipt_burger_successfull(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_receipt() == td.burger_receipt
