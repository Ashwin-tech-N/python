
import os
import shutil

def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Music": [".mp3", ".wav"],
        "Programs": [".py", ".java", ".cpp"]
    }

    if not os.path.isdir(folder_path):
        print("Folder does not exist!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        category = "Others"

        for folder, extensions in file_types.items():
            if extension in extensions:
                category = folder
                break

        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination = os.path.join(destination_folder, filename)

        if os.path.exists(destination):
            print("Skipped duplicate:", filename)
            continue

        shutil.move(file_path, destination)
        print("Moved", filename, "to", category)

    print("\nFile organization completed!")

path = input("Enter folder path: ")
organize_files(path)
