from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestData:

    bun_name = 'galactic_bun'
    bun_price = 100.0
    sauce = INGREDIENT_TYPE_SAUCE
    sauce_name = 'milk_sauce'
    sauce_price = 200.0
    filling = INGREDIENT_TYPE_FILLING
    filling_name = 'dark_matter_filling'
    filling_price = 300.0
    burger_cost = bun_price * 2.0 + sauce_price + filling_price
    burger_receipt = '(==== galactic_bun ====)\n= sauce milk_sauce =\n= filling dark_matter_filling =\n(==== galactic_bun ====)\n\nPrice: 700.0'
