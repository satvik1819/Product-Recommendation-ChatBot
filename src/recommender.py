from config import TOP_K
from src.category_filter import detect_category, filter_by_category
from src.product_filter import filter_products_only
import faiss
import numpy as np

class Recommender:
    def __init__(self, embedding_model, df):
        self.embedding_model = embedding_model
        self.df = df
        self.embeddings = embedding_model.embeddings

    def compute_score(self, query, product_name, description, distance):
        score = 0

        query = query.lower()
        product_name = str(product_name).lower()
        description = str(description).lower()

        score += 1 / (1 + distance)

        for word in query.split():
            if word in product_name:
                score += 0.5
            if word in description:
                score += 0.2

        if any(word in product_name for word in ["phone", "mobile", "smartphone"]):
            score += 1

        accessory_words = [
            'cover', 'case', 'charger', 'cable',
            'headset', 'earphone', 'screen guard',
            'tempered', 'holder', 'adapter',
            'power bank', 'usb', 'speaker'
        ]

        if any(word in product_name for word in accessory_words):
            score -= 2

        return score

    def recommend(self, query):
        category = detect_category(query)
        print(f"\nDetected Category: {category}")

        # Step 1: Filter dataframe
        filtered_df = filter_by_category(self.df, category)
        filtered_df = filter_products_only(filtered_df, query)

        if filtered_df.empty:
            filtered_df = self.df

        # Step 2: Get indices of filtered data
        filtered_indices = filtered_df.index.tolist()

        # Step 3: Select corresponding embeddings
        filtered_embeddings = self.embeddings[filtered_indices]

        # Step 4: Build FAISS only on subset (FAST)
        dimension = filtered_embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(filtered_embeddings))

        # Step 5: Encode query
        query_vec = self.embedding_model.encode_query(query)

        distances, indices = index.search(query_vec, TOP_K * 5)

        # Step 6: Map back to original dataframe
        actual_indices = [filtered_indices[i] for i in indices[0]]
        candidates = self.df.iloc[actual_indices].copy()
        candidates['distance'] = distances[0]

        # Step 7: Ranking
        candidates['score'] = candidates.apply(
            lambda row: self.compute_score(
                query,
                row['product_name'],
                row['clean_description'],
                row['distance']
            ),
            axis=1
        )

        results = candidates.sort_values(by='score', ascending=False).head(TOP_K)

        return results[['product_name', 'clean_description']]