import sys
import typing


def main():
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file {sys.argv[1]}")

    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError as e:
        print(e)
        return
    except PermissionError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        return

    context = file.read()
    print("---")
    print("")
    print(context)
    print("")
    print("---")

    file.close()
    print("File 'ancient_fragment.txt' closed.")

if __name__ == "__main__":
    main()