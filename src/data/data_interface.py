import pandas as pd

from .pinecone_interface import PineconeInterface
from .json_wrangler import JsonWrangler
from .tokenizer import Tokenizer


class DataInterface:
    """ DataInterface is a class that acts as an interface for handling data operations.

        It allows you to read JSON data from a file and convert it into a pandas DataFrame,
        write the DataFrame to a SQL or vector database, and perform lookups on the data. """

    def __init__(self):
        self.pinecone_interface = PineconeInterface()
        self.wrangler = JsonWrangler()
        self.tokenizer = Tokenizer()

    def upsert_coles_data(self, file_path, index_name):
        df = self.wrangler.json_to_dataframe(file_path)
        list_of_upserts, dimensions = self.wrangler.format_df_for_upsert(df)
        index_list = self.pinecone_interface.get_index_list()
        upsert_count = 0

        if index_name not in index_list:
            self.pinecone_interface.create_index(index_name=index_name, dimension=dimensions,
                                                 metric='euclidean')

        for item in list_of_upserts:
            upsert_count += 1
            self.pinecone_interface.upsert_to_index(index_name=index_name, vector_data=[item])
            # Vector data needs to be a tuple
            print("Upsert", upsert_count)

    def query_database(self, index_name, queries: iter) -> pd.DataFrame:
        results = list()
        for query in queries:
            vector_query = self.tokenizer.embed_string(query)
            matches = self.pinecone_interface.query_index(index_name=index_name, vector=vector_query, top_k=1,
                                                          include_values=False, include_metadata=True)
            result = matches["matches"][0]['metadata']
            results.append(result)
        results_df = pd.DataFrame(results)
        return results_df
