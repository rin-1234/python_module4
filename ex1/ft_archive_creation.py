import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file {sys.argv[1]}")

    try:
        file = open(sys.argv[1], "r")
    except Exception as e:
        print(e)
        return

    try:
        context = file.read()
    except Exception as e:
        print(e)
        file.close()
        return

    file.close()
    print(f"File {sys.argv[0]} closed.")

    print("")
    print("---")
    print("")
    print(context)
    print("")
    print("---")

    print("Transform data:")
    print("---")
    print("")
    new_context = []
    for line in context:
        tmp = line + "#"
        new_context.append(tmp)
        print(tmp)
    print("")
    print("---")

    new_file_name = input("Enter new file name (or empty):")
    if new_file_name is None:
        print("Not saving data.")
        return

    try:
        new_file = open(new_file_name, "w")
    except Exception as e:
        print(e)
        return

    try:
        new_file.write(new_context)
    except Exception as e:
        print(e)
        new_file.close()
        return

    new_file.close()
    print(f"Data saved in file {new_file_name}")


if __name__ == "__main__":
    main()
