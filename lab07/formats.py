def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.splitlines()]
    head = lines[0].split(',')
    return [dict(zip(head, line.split(','))) for line in lines[1:]]
print(csv_to_records("id,город
1,Азов
2,Шахты
"))
