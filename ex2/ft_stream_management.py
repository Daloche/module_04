import sys


def write_file(content_file: str) -> str:
    """Append a trailing marker to each line."""
    lines: list[str] = content_file.splitlines()
    transformed_lines: list[str] = [f"{line}#" for line in lines]
    result: str = "\n".join(transformed_lines)
    if content_file.endswith("\n") and transformed_lines:
        result += "\n"
    return result


def main() -> None:
    """Coordinate reading, transforming, and saving archive data."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    arg_value: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{arg_value}'")

    try:
        with open(arg_value, "r") as file:
            content = file.read()
        print(content, end="")
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{arg_value}': {e}",
            file=sys.stderr,
        )
        return

    print(f"File '{arg_value}' closed.")

    file_tmp: str = write_file(content)
    print("\nTransform data:")
    print(file_tmp, end="")

    print("Enter new file name (or empty): ", end="", flush=True)
    name_file: str = sys.stdin.readline().rstrip("\r\n")

    if name_file:
        print(f"Saving data to '{name_file}'")
        try:
            with open(name_file, "w") as new_file:
                new_file.write(file_tmp)
            print(f"Data saved in file '{name_file}'.")
        except OSError as e:
            print(
                f"[STDERR] Error opening file '{name_file}': {e}",
                file=sys.stderr,
            )
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
