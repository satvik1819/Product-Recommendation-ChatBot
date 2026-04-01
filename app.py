from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.embeddings import EmbeddingModel
from src.recommender import Recommender
from src.utils import print_results

def main():
    print("Loading data...")
    df = load_data()

    if df is None:
        return

    print("Preprocessing data...")
    df = preprocess_data(df)

    #  Build embeddings ONCE
    embedding_model = EmbeddingModel()
    embedding_model.build_embeddings(df['combined_text'].tolist())

    recommender = Recommender(embedding_model, df)

    print("\nSystem Ready! Type 'exit' to quit.\n")

    while True:
        query = input("Enter your query: ")

        if query.lower() == "exit":
            break

        results = recommender.recommend(query)
        print_results(results)


if __name__ == "__main__":
    main()