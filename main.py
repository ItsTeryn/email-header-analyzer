import sys
from analyzer.parser import load_header, get_basic_fields
from analyzer.hops import get_hops
from analyzer.auth import get_auth_results


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <header_file>")
        sys.exit(1)

    msg = load_header(sys.argv[1])

    print("=== Basic Fields ===")
    for name, value in get_basic_fields(msg).items():
        print(f"{name:12} {value}")

    print()
    print("=== Sender Path (first hop to last) ===")
    for hop in get_hops(msg):
        print(f"Hop {hop['hop']}: {hop['from']} ({hop['ip']}) -> {hop['by']}")

    print()
    print("=== Authentication Results ===")
    for check, result in get_auth_results(msg).items():
        print(f"{check.upper():6} {result}")


if __name__ == "__main__":
    main()
