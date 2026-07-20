from pathlib import Path


def secure_archive(
    name_file: str,
    file_mode: str = "r",
    message: str = "",
) -> tuple[bool, str]:
    """Open a file for reading or writing and return the operation result."""
    try:
        with open(name_file, file_mode) as file:
            if message:
                file.write(message)
                return True, message
            if "r" in file_mode or "+" in file_mode:
                return True, file.read()
            return True, ""
    except OSError as e:
        return False, str(e)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive(str(base_dir / "secure_archive"), "r"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive(str(base_dir / "ancient_fragment.txt"), "r"))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    mes = "'Content successfully written to file'"
    print(secure_archive(str(base_dir / "new_file.txt"), "w", mes))
