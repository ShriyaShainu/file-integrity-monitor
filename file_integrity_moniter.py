
import hashlib
import os


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()

    except OSError as error:
        print("Error reading file:", error)
        return None


def main():
    file_path = input("Enter the file path to monitor: ").strip().strip('"')

    if not os.path.isfile(file_path):
        print("File not found!")
        return

    reference_hash = calculate_sha256(file_path)

    if reference_hash is None:
        return

    print("\nReference SHA-256 hash:")
    print(reference_hash)

    while True:
        print("\n1. Check file integrity")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if not os.path.isfile(file_path):
                print("WARNING: File is missing!")
                continue

            current_hash = calculate_sha256(file_path)

            if current_hash is None:
                continue

            if current_hash == reference_hash:
                print("File integrity verified. No changes detected.")
            else:
                print("WARNING: File has been modified!")

        elif choice == "2":
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
