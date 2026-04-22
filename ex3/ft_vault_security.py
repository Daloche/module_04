def secure_archive(name_file: str, file_mose: str, messahe: str = "") -> tuple[bool, str]:
    my_bool = False
    try:
        file = open(name_file, file_mose)
        if file:
            my_bool = True
        if messahe:
            file.write(messahe)
            return my_bool, messahe
        else:
            return my_bool, file.read()
    except (FileNotFoundError, PermissionError) as e:
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
    print(secure_archive("new_file.txt", "w", "'Content successfully written to file'"))
