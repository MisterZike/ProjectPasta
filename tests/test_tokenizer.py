import unittest
import transformers
from src.data.tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    def test_tokenize_string(self):
        words = "Tokenize these words"
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize_string(string=words)
        # print("Test output:", tokens)

        self.assertIsInstance(obj=tokens, cls=list)
        for item in tokens:
            self.assertIsInstance(item, str)

    def test_embed_string(self):
        sentence = "The sky is blue"
        tokenizer = Tokenizer()
        vector_embeddings = tokenizer.embed_string(string=sentence)

        self.assertIsInstance(obj=vector_embeddings, cls=list)
        for item in vector_embeddings:
            self.assertIsInstance(item, float)
