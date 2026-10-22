def count_items(values: list) -> dict:
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def unique_sorted(values: list) -> list:
    return sorted(set(values))

def common(first: list, second: list) -> list:
    return sorted(set(first) & set(second))

def only_in_first(first: list, second: list) -> list:
    return sorted(set(first) - set(second))