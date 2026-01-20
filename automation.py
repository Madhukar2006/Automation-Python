import os
import shutil
from datetime import datetime

LOG_FILE = "automation.log"

def write_log(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

def organize_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("Folder not found.")
            return

        file_types = {
            "Images": [".jpg", ".png", ".jpeg"],
            "Documents": [".pdf", ".txt", ".docx"],
            "Music": [".mp3", ".wav"],
            "Others": []
        }

        for folder in file_types:
            os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                moved = False
                for category, extensions in file_types.items():
                    if any(file.lower().endswith(ext) for ext in extensions):
                        new_path = os.path.join(folder_path, category, file)
                        shutil.move(file_path, new_path)
                        write_log(f"Moved {file} to {category}")
                        moved = True
                        break

                if not moved:
                    shutil.move(file_path, os.path.join(folder_path, "Others", file))
                    write_log(f"Moved {file} to Others")

        print("File organization completed successfully.")

    except Exception as e:
        write_log(f"Error: {str(e)}")
        print("An error occurred. Check log file.")

if __name__ == "__main__":
    path = input("Enter folder path to organize: ")
    organize_files(path)
