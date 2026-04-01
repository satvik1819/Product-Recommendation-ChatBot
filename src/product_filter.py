def filter_products_only(df, query):
    query = query.lower()

    # If query is about phones → remove accessories
    if any(word in query for word in ["phone", "mobile", "smartphone"]):

        exclude_keywords = [
            'cover', 'case', 'charger', 'cable',
            'headset', 'earphone', 'screen guard',
            'tempered', 'holder', 'adapter',
            'power bank', 'usb'
        ]

        for word in exclude_keywords:
            df = df[~df['product_name'].str.contains(word, case=False, na=False)]

    return df