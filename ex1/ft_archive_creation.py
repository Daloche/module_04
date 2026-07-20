import sys
import typing


def main() -> None:
    """Load a file, transform each line, and optionally save the result."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    arg_value = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{arg_value}'")

    file: typing.Optional[typing.IO[str]] = None
    content: str = ""
    try:
        file = open(arg_value, "r")
        content = file.read()
        print(content, end="")
    except OSError as e:
        print(f"Error opening file '{arg_value}': {e}")
        return  # On quitte si on ne peut pas lire le fichier source
    finally:
        if file is not None:
            file.close()
            print(f"File '{arg_value}' closed.")

    # Transformation : ajouter '#' à la fin de chaque ligne non vide
    lines = content.splitlines()
    transformed_lines = [f"{line}#" for line in lines]
    result = "\n".join(transformed_lines)
    if content.endswith("\n") and transformed_lines:
        result += "\n"

    print("\nTransform data:")
    print(result, end="")

    try:
        name_file: str = input("Enter new file name (or empty): ")
    except EOFError:
        name_file = ""

    if name_file:
        print(f"Saving data to '{name_file}'")
        new_file: typing.Optional[typing.IO[str]] = None
        try:
            new_file = open(name_file, "w")
            new_file.write(result)
            print(f"Data saved in file '{name_file}'.")
        except OSError as e:
            print(f"Error saving file '{name_file}': {e}")
        finally:
            if new_file is not None:
                new_file.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
