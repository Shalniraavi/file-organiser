import os
import shutil

# Function to organize a specific file
def organize_file(file_path):
    # Check if the provided path is a file
    if not os.path.isfile(file_path):
        print(f"The path '{file_path}' is not a valid file.")
        return

    # Get the directory of the provided file
    directory = os.path.dirname(file_path)

    # Dictionary to categorize file types
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".tar", ".rar", ".gz"],
    }

    moved = False
    # Check file extension and move to the corresponding folder
    for folder_name, extensions in file_types.items():
        if os.path.basename(file_path).lower().endswith(tuple(extensions)):
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, os.path.basename(file_path)))
            moved = True
            break

    # Move to 'Others' folder if it doesn't match any specified file type
    if not moved:
        other_folder = os.path.join(directory, "Others")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(other_folder, os.path.basename(file_path)))

# Prompt the user for the file path
file_to_organize = input("Enter the full path of the file to organize: ").strip('"')

# Run the function with the provided file path
organize_file(file_to_organize)
print("File organized successfully!")
