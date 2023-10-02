import unittest
import pandas as pd

from src.data.json_wrangler import JsonWrangler


class TestJsonWrangler(unittest.TestCase):
    def test_json_to_dataframe(self):
        fp = r"C:\Users\Ezekiel\PycharmProjects\ProjectPasta\src\data\test.json"
        wrangler = JsonWrangler()
        df = wrangler.json_to_dataframe(fp)
        print(df)

    def test_vectorize_dataframe(self):
        fp = r"C:\Users\Ezekiel\PycharmProjects\ProjectPasta\src\data\test.json"
        wrangler = JsonWrangler()
        df = wrangler.json_to_dataframe(fp)
        upsert_data = wrangler.vectorize_dataframe(df)
        print(upsert_data)
        self.assertIsInstance(upsert_data, pd.DataFrame)

    def test_format_df_for_upsert(self):
        fp = r"C:\Users\Ezekiel\PycharmProjects\ProjectPasta\src\data\test.json"
        wrangler = JsonWrangler()
        df = wrangler.json_to_dataframe(fp)
        dicts, dimensions = wrangler.format_df_for_upsert(df)
        # print("Vector dimension is:", dimensions)
        for num in dicts[0]["values"]:
            self.assertIsInstance(num, float)
         # print(type(dicts[0]["values"]))

