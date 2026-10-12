def parse_record(line: str) -> dict:
    if not line or not line.strip():
        raise ValueError("Пустая строка")

    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Неверное количество полей (должно быть ровно 3)")

    city, temp_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")

    try:
        normalized_temp = temp_str.replace(",", ".")
        temp = float(normalized_temp)
    except ValueError:
        raise ValueError(f"Некорректная температура: '{temp_str}' не является числом")

    return {
        "city": city,
        "temperature": temp,
        "date": date
    }


def read_valid(lines: list[str]) -> list[dict]:

    valid_records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass

    return valid_records


def average_by_city(records: list[dict]) -> dict:

    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temp = record["temperature"]
        totals[city] = totals.get(city, 0.0) + temp
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        avg = totals[city] / counts[city]
        averages[city] = round(avg, 1)

    return averages


def warmest_city(records: list[dict]) -> str:

    if not records:
        return ""

    averages = average_by_city(records)


    sorted_cities = sorted(averages.keys(), key=lambda c: (-averages[c], c))

    return sorted_cities[0]