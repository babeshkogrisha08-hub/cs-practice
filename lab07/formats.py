def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.splitlines()]
    head = lines[0].split(',')
    return [dict(zip(head, line.split(','))) for line in lines[1:]]




def parse_settings(lines: list[str]) -> dict:
    res = {}
    key = ''
    for line in lines:
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        if line[0] == "-":
            raw = line[2:].strip()
            flag = True
        else:
            key, raw = line.split(':', 1)
            key = key.strip()
            raw = raw.strip()
            flag = False
            if raw == '':
                res[key] = []
                continue
        low = raw.lower()
        if low in ('true'):
            val = True
        elif low in ("false", "no"):
            val = False
        else:
            val = raw
        if flag:
            res[key].append(val)
        else:
            res[key] = val
    return res