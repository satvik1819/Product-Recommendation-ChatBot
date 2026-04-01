from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from config import EMBEDDING_MODEL

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.embeddings = None

    def build_embeddings(self, texts):
        print("Building embeddings...")
        self.embeddings = self.model.encode(texts, show_progress_bar=True)

    def encode_query(self, query):
        return self.model.encode([query])