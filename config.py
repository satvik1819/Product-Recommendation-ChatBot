import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "flipkart_com-ecommerce_sample.csv")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

TOP_K = 5