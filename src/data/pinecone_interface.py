import pinecone


class PineconeInterface:
    def __init__(self):
        self.apikey = "dfa7897f-3ca4-4955-a448-fdd8be053d47"
        self.environment = "asia-southeast1-gcp-free"

    def get_index_list(self) -> list:
        pinecone.init(api_key=self.apikey, environment=self.environment)
        return pinecone.list_indexes()

    def create_index(self, index_name, dimension, metric):
        pinecone.init(api_key=self.apikey, environment=self.environment)
        print("Creating index. This may take a few minutes...")
        pinecone.create_index(name=index_name, dimension=dimension, metric=metric)
        print(f"Index {index_name} created successfully")
        pinecone.describe_index(name=index_name)

    def upsert_to_index(self, index_name, vector_data):
        pinecone.init(api_key=self.apikey, environment=self.environment)
        index = pinecone.Index(index_name)
        index.upsert(vector_data)
        # print(index.describe_index_stats())

    def query_index(self, index_name, vector, top_k: int, include_values: bool, include_metadata: bool) -> pinecone.QueryResponse:
        pinecone.init(api_key=self.apikey, environment=self.environment)
        index = pinecone.Index(index_name)
        matches = index.query(vector=vector, top_k=top_k, include_values=include_values,
                              include_metadata=include_metadata)
        return matches

    def delete_index(self, index_name):
        pinecone.init(api_key=self.apikey, environment=self.environment)
        pinecone.delete_index(index_name)
        print(f"Index '{index_name}' deleted.")
