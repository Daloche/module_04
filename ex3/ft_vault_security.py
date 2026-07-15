def secure_archive(name_file: str,
                   file_mode: str = "r",
                   message: str = "") -> tuple[bool, str]:
    """Open a file for reading or writing and return the operation result."""
    my_bool = False
    try:
        with open(name_file, file_mode) as file:
            if file:
                my_bool = True
            if message and 'w' in file_mode:
                file.write(message)
                return my_bool, message
            else:
                return my_bool, file.read()
    except (OSError) as e:
        return my_bool, str(e)


if __name__ == "__main__":
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("secure_archive", "r"))
    print("\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("test.txt", "r"))
    print("\n")

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print("\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    mes = "'Content successfully written to file'"
    print(secure_archive("new_file.txt", "w", mes))
