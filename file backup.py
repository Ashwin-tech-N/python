import os
import shutil
from datetime import datetime

source_folder = input("Enter folder path to backup: ")
backup_folder = input("Enter backup destination: ")

if not os.path.exists(source_folder):
    print("Source folder does not exist!")

else:
    os.makedirs(backup_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"

    destination = os.path.join(backup_folder, backup_name)

    shutil.copytree(source_folder, destination)

    print("Backup completed successfully!")
    print("Backup location:", destination)
