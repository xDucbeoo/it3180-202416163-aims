def search_by_title(cart, keyword):
    keyword = keyword.strip().lower()

    if not keyword:
        return []

    results = []

    for dvd in cart.items:
        if keyword in dvd.title.lower():
            results.append(dvd)

    return results