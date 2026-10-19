VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError()
    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError()
    time_str, level, message = parts
    if level not in VALID_LEVELS:
        raise ValueError()
    return {"time": time_str, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        try:
            event = parse_event(line_clean)
            lvl = event["level"]
            counts[lvl] = counts.get(lvl, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
    return counts

def top_errors(lines, n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        try:
            event = parse_event(line_clean)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
    sorted_errors = sorted(
        error_counts.items(),
        key=lambda item: (-item[1], item[0])
    )
    return [[msg, count] for msg, count in sorted_errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for msg, count in errors:
        lines.append(f"- {msg} — {count}")
    return "\n".join(lines) + "\n"