import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file: IO[str] = open(file_name, "r")
    except Exception as e:
        print(f"[STDERR] Error opening file '{file_name}': {e}",
              file=sys.stderr)
        return

    try:
        content = file.read()
    except Exception as e:
        print(f"[STDERR] Error reading file '{file_name}': {e}",
              file=sys.stderr)
        file.close()
        return

    print("---")
    print("")
    print(content)
    print("---")

    file.close()
    print(f"File '{file_name}' closed.")

    print("")
    print("Transform data:")
    print("---")
    print("")
    new_content = ""
    for line in content.splitlines():
        new_content += line + "#\n"
    print(new_content)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    try:
        new_file_name = sys.stdin.readline().strip()
    except KeyboardInterrupt:
        print("")
        new_file_name = ""
    if new_file_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file_name}'")
    try:
        new_file: IO[str] = open(new_file_name, "w")
    except Exception as e:
        print(f"[STDERR] Error opening file '{new_file_name}': {e}",
              file=sys.stderr)
        print("Data not saved.")
        return

    try:
        new_file.write(new_content)
    except Exception as e:
        print(f"[STDERR] Error writing file '{new_file_name}': {e}",
              file=sys.stderr)
        print("Data not saved.")
        new_file.close()
        return

    new_file.close()
    print(f"Data saved in file '{new_file_name}'.")


if __name__ == "__main__":
    main()
