import sys
from stats import average_by_city, read_valid, warmest_city
def main():
    lines = sys.stdin.read().splitlines()
    valid_records = read_valid(lines)
    non_empty_lines = [l for l in lines if l.strip()]
    error_count = len(non_empty_lines) - len(valid_records)
    warmest = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    warmest_avg = averages.get(warmest, 0.0)
    print(len(valid_records))
    print(error_count)
    print(f"{warmest_avg:.1f}")

if __name__ == "__main__":
    main()
