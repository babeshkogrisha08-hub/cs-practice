def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) < 2:
        return []
    head = head = [h.strip() for h in lines[0].split(',')]
    return [dict(zip(head, [v.strip() for v in line.split(',')])) for line in lines[1:]]




def parse_settings(lines: list[str]) -> dict:
    res = {}
    key = ''
    for line in lines:
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        if line[0] == "-":
            raw = line[1:].strip()
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
        num = raw.replace(',', '.', 1)
        if low in ('true', 'yes'):
            val = True
        elif low in ("false", "no"):
            val = False
        elif raw.lstrip('-').isdigit():
            val = int(raw)
        elif num.lstrip('-').replace('.', '', 1).isdigit():
            val = float(num)
        else:
            val = raw
        if flag:
            res[key].append(val)
        else:
            res[key] = val
    return res




def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:  # 1. "id" в кавычках
    res = []
    for row in rows:
        cop = row.copy()
        k = row.get(key)
        if k in extra:
            cop.update(extra[k])
        res.append(cop)
    return res


def records_to_json(records: list[dict]) -> str:
    if not records:
        return "[]"
    text = []
    for rec in records:
        pairs = []
        for k in sorted(rec):
            v = rec[k]
            clean = str(v).replace('"', '\\"')
            val = f'"{clean}"'
            pairs.append(f'    "{k}": {val}')
        text.append("  {\n" + ",\n".join(pairs) + "\n  }")
    return "[\n" + ",\n".join(text) + "\n]"