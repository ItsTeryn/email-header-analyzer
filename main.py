import sys
from analyzer.parser import load_header, get_basic_fields


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <header_file>")
		sys.exit(1)
		
	msg = load_header(sys.argv[1])
	
	for name, value in get_basic_fields(msg).items():
		print(f"{name:12} {value}")


if __name__ == "__main__":
	main()
