import re

def clean_description(text):
    text = str(text).lower()

    text = re.sub(r'\b(rs\.?|inr)?\s?\d+\b', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    noise_words = [
        'buy', 'product', 'flipkart', 'amazon', 'free', 'shipping',
        'replacement', 'guarantee', 'warranty', 'cash', 'delivery',
        'online', 'only', 'offer', 'best', 'sale', 'discount',
        'genuine', 'original', 'brand', 'new', 'day'
    ]

    words = text.split()
    words = [w for w in words if w not in noise_words and len(w) > 2]

    return " ".join(words)


def preprocess_data(df):
    cols = ['product_name', 'description', 'product_category_tree']
    df = df[cols].dropna()

    df['clean_description'] = df['description'].apply(clean_description)

    df['combined_text'] = (
        "PRODUCT: " +
        df['product_name'] + " " +
        df['clean_description'] + " " +
        df['product_category_tree']
    )

    df = df.reset_index(drop=True)

    return df