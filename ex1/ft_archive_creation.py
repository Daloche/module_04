import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    arg_value = sys.argv[1]
    print(f"Accessing file '{arg_value}'")
    try:
        file: typing.IO[str] = open(arg_value, "r")
        print("___\n")
        content = file.read()
        split_content = content.split("\n")
        for i in range(len(split_content)):
            split_content[i] += "#"
        print(content)
        print("___")
        file.close()
        print(f"File '{arg_value}' closed.", end="\n\n")
        print("Transform data:")
        print("___\n")
        file_tmp = "\n".join(split_content)
        print(file_tmp)
        print("___")
        name_file = input("Enter new file name (or empty): ")
        if name_file:
            new_file = open(name_file, "w")
            new_file.write(file_tmp)
            print(f"Saving data to '{name_file}'")
            print(f"Data saved in file '{name_file}'")
        else:
            print("Not saving data")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file {arg_value} : {e}")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()
