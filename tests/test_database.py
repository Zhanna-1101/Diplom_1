from praktikum.database import Database


class TestDatabase:

    def test_available_buns_in_database_successfull(self):
        database = Database()

        assert len(database.buns) == 3

    def test_available_ingredients_in_database_successfull(self):
        database = Database()

        assert len(database.ingredients) == 6
