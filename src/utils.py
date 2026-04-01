def print_results(results):
    print("\nTop Recommendations:\n")

    for i, row in results.iterrows():
        print(f"Product: {row['product_name']}")
        print(f"Description: {row['clean_description'][:150]}...")
        print("-" * 50)