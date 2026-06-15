import sys


def main() -> None:
    """Read a file path from the command line and display its contents."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    arg_value = sys.argv[1]
    print(f"Accessing file '{arg_value}'")
    try:
        print("___\n")
        with open(arg_value, "r") as file:
            print(file.read())
        print("___")
        print(f"File '{arg_value}' closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file {arg_value} : {e}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()
