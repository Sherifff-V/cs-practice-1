def read_rows(lines):
    header = None
    rows = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = [part.strip() for part in line.split(",")]

        if header is None:
            header = parts
            continue

        if len(parts) != len(header):
            continue

        rows.append(dict(zip(header, parts)))

    return rows


def count_types(rows):
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows, kind):
    total = 0.0

    for row in rows:
        if row.get("тип") != kind:
            continue

        value = row.get("минуты", "").strip().replace(",", ".")
        try:
            total += float(value)
        except ValueError:
            continue

    return round(total, 1)


def to_csv(counts):
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"