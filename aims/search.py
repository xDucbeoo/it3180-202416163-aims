
def search_by_category(cart, category):
    category = category.strip().lower()

    if not category:
        return []

    results = []

    for dvd in cart.items:
        if dvd.category.strip().lower() == category:
            results.append(dvd)

    return results


def search_by_title(cart, keyword):
    keyword = keyword.strip().lower()

    if not keyword:
        return []

    results = []

    for dvd in cart.items:
        if keyword in dvd.title.lower():
            results.append(dvd)

    return results
