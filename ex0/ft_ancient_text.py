import sys
import typing


def main() -> None:
    """Read a file path from the command line and display its contents."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    arg_value: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{arg_value}'")

    try:
        file: typing.IO[str] = open(arg_value, "r")
    except OSError as e:
        print(f"Error opening file '{arg_value}': {e}")
        return

    try:
        content = file.read()
        print("---")
        print()
        print(content, end="")
        if not content.endswith("\n"):
            print()
        print()
        print("---")
    finally:
        file.close()
        print(f"File '{arg_value}' closed.")


if __name__ == "__main__":
    main()
