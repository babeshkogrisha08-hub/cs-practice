from logstats import count_levels, format_report, top_errors

def main() -> None:
    filename = input().strip()
    with open(filename, "r", encoding="utf-8") as f:
        counts = count_levels(f)
    with open(filename, "r", encoding="utf-8") as f:
        errors = top_errors(f, n=10)
    total_lines = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)
    print(total_lines)
    print(error_count)
    print(broken_count)
    report_text = format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)


if __name__ == "__main__":
    main()