def secure_archive(
    name_file: str, mode: str = "r", message: str = ""
) -> tuple[bool, str]:
    """Open a file for reading or writing securely using a context manager."""
    try:
        with open(name_file, mode) as file:
            if "w" in mode or "a" in mode:
                file.write(message)
                return True, "Content successfully written to file"
            else:
                return True, file.read()
    except OSError as e:
        # Renvoie False accompagné du message d'erreur système
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    # On suppose ici que le fichier 'ancient_fragment.txt' existe pour le test
    print(secure_archive("ancient_fragment.txt", "r"))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", "Test content"))
