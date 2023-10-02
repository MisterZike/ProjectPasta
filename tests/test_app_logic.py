import unittest
import pandas as pd
from src.application.app_logic import AppLogic


class TestAppLogic(unittest.TestCase):
    def setUp(self):
        self.app = AppLogic()
        self.recipe = ''
        self.ingredients = ''

    def test_dish_lookup_and_list_ingredients(self):
        # Test lookup
        self.recipe = self.app.dish_lookup(dish_name='Pad Thai', unit_of_measure='metric', serving_size='4')
        print(self.recipe)
        self.assertIsInstance(self.recipe, str) and self.assertTrue(self.recipe)

        # Test list ingredients
        self.ingredients = self.app.list_ingredients(self.recipe)
        print(self.ingredients)
        self.assertIsInstance(self.ingredients, list) and self.assertTrue(self.ingredients)

        # Test DB query
        # shopping_list_df = self.app.query_db(self.ingredients)
        # print(shopping_list_df)
        # self.assertIsInstance(shopping_list_df, pd.DataFrame)


