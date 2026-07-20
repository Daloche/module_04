import sys
import typing


def main() -> None:
    """Read a file path from the command line and display its contents."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    arg_value = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{arg_value}'")

    file: typing.Optional[typing.IO[str]] = None
    try:
        file = open(arg_value, "r")
        print(file.read(), end="")
    except OSError as e:
        print(f"Error opening file '{arg_value}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{arg_value}' closed.")


if __name__ == "__main__":
    main()
