from transformers import AutoTokenizer
from sentence_transformers import SentenceTransformer


class Tokenizer:
    """This class handles the tokenization of words and sentences"""
    def __init__(self):
        self.word_tokenizer = AutoTokenizer.from_pretrained('transfo-xl-wt103')  # transfo-xl tokenizer uses word-level encodings
        self.sentence_embedder = SentenceTransformer('flax-sentence-embeddings/all_datasets_v3_mpnet-base')

    def tokenize_string(self, string) -> list[str]:
        tokens = self.word_tokenizer.tokenize(string.lower())
        return tokens

    def embed_string(self, string) -> list[float]:
        vector_encodings = self.sentence_embedder.encode(string).tolist()
        return vector_encodings
