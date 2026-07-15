import sys
import typing


def main() -> None:
    """Load a file, transform each line, and optionally save the result."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    arg_value = sys.argv[1]
    print(f"Accessing file '{arg_value}'")
    file: typing.Optional[typing.IO[str]] = None
    try:
        file = open(arg_value, 'r')
        content: str = file.read()
        print("---")
        print(content)
        print("---")
    except OSError as e:
        print(f"Error opening file '{arg_value}': {e}")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{arg_value}' closed.")

    file_tmp: list[str] = content.splitlines()
    result_tmp: list[str] = [f"{line}#" for line in file_tmp]
    result: str = "\n".join(result_tmp)
    result += "\n"
    print("\nTransform data:")
    print('---')
    print(result, end='')
    print('---')

    name_file = input("Enter new file name (or empty): ")
    if name_file:
        try:
            new_file = open(name_file, "w")
            new_file.write(result)
            print(f"Data saved in file '{name_file}'.")
        except OSError as e:
            print(f"Error saving file {name_file}: {e}")
        finally:
            new_file.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()
