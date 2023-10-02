import pandas as pd

from .tokenizer import Tokenizer


class JsonWrangler:
    def __init__(self):
        self.df = pd.DataFrame()
        self.tokenizer = Tokenizer()

    def json_to_dataframe(self, json_fp) -> pd.DataFrame:
        # Read json data into a dataframe
        data = pd.read_json(json_fp)
        data_list = data["Data"]
        dataframe = pd.DataFrame.from_records(data_list)
        self.df = dataframe
        return dataframe

    def vectorize_dataframe(self, df):
        vectorized_df = pd.DataFrame()

        # Prepare Vector IDs
        vector_ids = range(len(df))
        vector_ids = pd.Series(vector_ids)
        vector_ids = vector_ids.apply(lambda x: x + 1)
        vector_ids = vector_ids.apply(lambda x: "vec" + str(x))
        vectorized_df["id"] = vector_ids

        # Prepare Vectorized Values
        print("Creating vector embeddings. This may take a few minutes...")
        vectorized_df["values"] = df["product_name"]
        vectorized_df["values"] = vectorized_df["values"].apply(lambda x: self.tokenizer.embed_string(x))
        print("Vector embeddings ready.")

        # Prepare Metadata
        print("Preparing metadata")
        df["product_name"] = df["product_name"].apply(lambda x: {"item": str(x)})
        df["price"] = df["price"].apply(lambda x: {"price": str(x)})
        vectorized_df["metadata"] = df.apply(
            lambda row: {**row["title"], **row["price"]}, axis=1)
        print("Metadata ready.")

        return vectorized_df

    def format_df_for_upsert(self, df):
        vectorized_df = pd.DataFrame()

        # Prepare Vector IDs
        print("Preparing data...")
        vector_ids = range(len(df))
        vector_ids = pd.Series(vector_ids)
        vector_ids = vector_ids.apply(lambda x: x + 1)
        vector_ids = vector_ids.apply(lambda x: "vec" + str(x))
        vectorized_df["id"] = vector_ids

        # Prepare Vectorized Values
        print("Creating vector embeddings. This may take a few minutes...")
        vectorized_df["values"] = df["product_name"]
        vectorized_df["values"] = vectorized_df["values"].apply(lambda x: self.tokenizer.embed_string(x))

        # Prepare Metadata
        print("Preparing metadata...")
        df["product_name"] = df["product_name"].apply(lambda x: {"item": str(x)})
        df["price"] = df["price"].apply(lambda x: {"price": str(x)})
        vectorized_df["metadata"] = df.apply(
            lambda row: {**row["product_name"], **row["price"]}, axis=1)

        # Return list of dicts
        list_of_dicts = vectorized_df.to_dict(orient='records')

        # Return length of values
        dimensions = len(vectorized_df.iloc[0]["values"])
        return list_of_dicts, dimensions
