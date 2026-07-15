import sys
import typing


def open_file(name_file: str) -> str:
    """Open a text file, read all its content, and close the file."""
    file: typing.Optional[typing.IO[str]] = None
    content: str = ""
    try:
        file = open(name_file, "r")
        content = file.read()
    except OSError:
        pass
    finally:
        if file is not None:
            file.close()
    return content


def write_file(content_file: str) -> str:
    """Append a trailing marker to each line except the last one."""
    split_content: list[str] = content_file.split("\n")
    for i in range(len(split_content)):
        split_content[i] += "#"
    result = "\n".join(split_content)
    result += "\n"
    return result


def saving_data(name_other_file: str, content_new_file: str) -> None:
    """Save transformed content to a file when a destination is provided."""
    new_file: typing.Optional[typing.IO[str]] = None
    try:
        if name_other_file:
            print(f"Saving data to '{name_other_file}'")
            new_file = open(name_other_file, "w")
            new_file.write(content_new_file)
            print(f"Data saved in file '{name_other_file}'")
        else:
            print("Not saving data")
    except (OSError) as e:
        mes = f"[STDERR] Error opening file {name_other_file} : {e}"
        print(mes, file=sys.stderr)
        print("Not saving data")
    finally :
        if new_file is not None:
            new_file.close()

def main() -> None:
    """Coordinate reading, transforming, and saving archive data."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    arg_value = sys.argv[1]
    print(f"Accessing file '{arg_value}'")
    try:
        print("---\n")
        content = open_file(arg_value)
        print(content)
        print("---")
        print(f"File '{arg_value}' closed.", end="\n\n")
        print("Transform data:")
        print("---\n")
        file_tmp = write_file(content)
        print(file_tmp)
        print("---")
        print("Enter new file name (or empty)", end=": ", flush=True)
        name_file: str = sys.stdin.readline().strip()
        saving_data(name_file, file_tmp)
    except (OSError) as e:
        mes = f"[STDERR] Error opening file {arg_value} : {e}"
        print(mes, file=sys.stderr)


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()
