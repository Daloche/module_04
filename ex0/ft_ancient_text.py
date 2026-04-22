import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    arg_value = sys.argv[1]
    print(f"Accessing file '{arg_value}'")
    try:
        file = open(arg_value, "r")
        print("___\n")
        print(file.read())
        file.close()
        print("___")
        print(f"File '{arg_value}' closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file {arg_value} : {e}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()
