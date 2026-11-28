

class Operation(Enum):
    READ = 0
    WRITE = 1

def secure_archive(
    file_name: str,
    operation: int,
    output_context: str | None
) -> tuple[bool, str]:
    if Operation.READ == operation:
        try:
            with open(file_name, "r") as file:
                context = file.read()
        except FileNotFoundError as e:
            print("Using 'secure_archive' to read from a nonexistent file:")
            return (False, e)
        except PermissionError as e:
            print("Using 'secure_archive' to read from an inaccessible file:")
            return (False, e)
        except Exception as e:
            print("Error occur")
            return (False, e)

        print("Using 'secure_archive' to read from a regular file:")
        return (True, context)

    elif Operation.WRITE == operation:
        try:
            with open(file_name, "w") as file:
                file.write(output_context)
        except Exception as e:
            print("Error occur")
            return [False, e]

        print("Using 'secure_archive' to write previous content to a new file:")
        return (True, "'Content successfully written to file'")

    else:
        return [False, f"Invalid operation: {operation}"]




def main() -> None:
    print("=== Cyber Archives Security ===")
    
    result = secure_archive("/not/nonexisting/file", Operation.READ)
    print(result)
    result = secure_archive("/etc/shadow", Operation.READ)
    print(result)
    result = secure_archive("./ancient_fragment.txt", Operation.READ)
    print(result)
    output = secure_archive("./new_file.txt", Operation.WRITE, result.value())
    print(output)


if __name__ == "__main__":
    main()
