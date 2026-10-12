def parse_record(line: str) -> dict:
    if not line or not line.strip():
        raise ValueError("Пустая строка")

    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Неверное количество полей")

    city, temp_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректная температура: '{temp_str}'")

    return {
        "city": city,
        "temperature": temp,
        "date": date
    }