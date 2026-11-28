def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(file_name, "r") as file:
                return (True, file.read())
        except Exception as e:
            return (False, str(e))
    elif action == "write":
        try:
            with open(file_name, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))
    return (False, f"Invalid action: '{action}'")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print("")

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print("")

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1]))
    else:
        print("Nothing to write: previous read failed.")


if __name__ == "__main__":
    main()
