import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
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

    print("---")
    print("")
    print(context)
    print("")
    print("---")

    file.close()
    print(f"File {sys.argv[0]} closed.")


if __name__ == "__main__":
    main()
