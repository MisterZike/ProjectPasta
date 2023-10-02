import unittest
import pandas as pd

from src.data.data_interface import DataInterface


class TestDataInterface(unittest.TestCase):
    def test_upsert_coles_data(self):
        interface = DataInterface()
        fp = r"C:\Users\Ezekiel\PycharmProjects\ProjectPasta\src\data\test.json"
        interface.upsert_coles_data(file_path=fp, index_name='coles-data')

    def test_query_database(self):
        interface = DataInterface()
        queries = ['raw prawns', 'fresh garlic', 'fresh shallots', 'fresh eggs']
        results = interface.query_database('coles-data', queries)
        print(results)
        self.assertIsInstance(results, pd.DataFrame)

# ['rice noodles', 'chicken breast', 'prawns', 'garlic', 'shallots', 'eggs', 'bean sprouts', 'firm tofu', 'roasted peanuts', 'fish sauce', 'tamarind paste', 'sugar', 'lime juice', 'chili powder', 'paprika', 'coriander leaves', 'lime wedges']