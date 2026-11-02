
import os
import hashlib

def get_file_hash(filepath):
    hasher = hashlib.sha256()

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


def find_duplicates(folder):
    files = {}
    duplicates = []

    for root, _, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(root, filename)

            try:
                file_hash = get_file_hash(path)

                if file_hash in files:
                    duplicates.append((path, files[file_hash]))
                else:
                    files[file_hash] = path

            except (OSError, PermissionError):
                print("Cannot access:", path)

    return duplicates


folder = input("Enter folder path: ")

if os.path.isdir(folder):
    result = find_duplicates(folder)

    if result:
        print("\nDuplicate files found:")
        for duplicate, original in result:
            print("Duplicate:", duplicate)
            print("Original:", original)
            print("--------------------")
    else:
        print("No duplicate files found.")
else:
    print("Invalid folder path.")
