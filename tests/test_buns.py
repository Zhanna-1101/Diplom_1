from praktikum.bun import Bun
from data import TestData as td


class TestBuns:

    def test_get_name_bun_successfull(self):
        bun = Bun(td.bun_name, td.bun_price)
        assert bun.get_name() == td.bun_name

    def test_get_price_bun_successfull(self):
        bun = Bun(td.bun_name, td.bun_price)
        assert bun.get_price() == td.bun_price
