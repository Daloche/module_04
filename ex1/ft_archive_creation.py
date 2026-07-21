import sys
import typing


def main() -> None:
    """Load a file, transform each line, and optionally save the result."""
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    arg_value: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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

    # Transformation : ajouter '#' à la fin de chaque ligne
    lines = content.splitlines()
    transformed_lines = [f"{line}#" for line in lines]
    result = "\n".join(transformed_lines)
    if content.endswith("\n") and transformed_lines:
        result += "\n"

    print("\nTransform data:")
    print("---")
    print()
    print(result, end="")
    if not result.endswith("\n"):
        print()
    print()
    print("---")

    try:
        name_file: str = input("Enter new file name (or empty): ")
    except EOFError:
        name_file = ""

    if name_file:
        print(f"Saving data to '{name_file}'")
        try:
            new_file: typing.IO[str] = open(name_file, "w")
        except OSError as e:
            print(f"Error opening file '{name_file}': {e}")
            print("Data not saved.")
            return
        try:
            new_file.write(result)
            print(f"Data saved in file '{name_file}'.")
        finally:
            new_file.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
