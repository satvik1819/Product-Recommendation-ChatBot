import pandas as pd
from config import DATA_PATH

def load_data():
    try:
        df = pd.read_csv(DATA_PATH)
        print(f"Dataset loaded: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None