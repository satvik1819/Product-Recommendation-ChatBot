def detect_category(query):
    query = query.lower()

    if any(word in query for word in ["phone", "mobile", "smartphone"]):
        return "mobile"
    elif any(word in query for word in ["laptop", "computer"]):
        return "laptop"
    elif any(word in query for word in ["shoe", "sneaker", "footwear"]):
        return "footwear"
    elif any(word in query for word in ["shirt", "tshirt", "dress", "clothing"]):
        return "clothing"
    elif any(word in query for word in ["watch"]):
        return "watch"

    return "all"


def filter_by_category(df, category):
    if category == "mobile":
        return df[df['product_category_tree'].str.contains("Mobile", case=False, na=False)]

    elif category == "laptop":
        return df[df['product_category_tree'].str.contains("Laptop", case=False, na=False)]

    elif category == "footwear":
        return df[df['product_category_tree'].str.contains("Footwear|Shoe", case=False, na=False)]

    elif category == "clothing":
        return df[df['product_category_tree'].str.contains("Clothing|Apparel", case=False, na=False)]

    elif category == "watch":
        return df[df['product_category_tree'].str.contains("Watch", case=False, na=False)]

    return df