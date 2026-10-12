import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    valid_records, error_count = read_valid(lines)

    warmest = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    warmest_avg = averages.get(warmest, 0.0)

    print(len(valid_records))
    print(error_count)
    print(f"{warmest_avg:.1f}")


if __name__ == "__main__":
    main()