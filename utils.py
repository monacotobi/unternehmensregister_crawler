import os
import shutil

def get_most_recent_download():
    # Path to the Downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")

    # Get list of all PDF files in the Downloads folder
    files = [os.path.join(downloads_folder, f) for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f)) and f.lower().endswith('.pdf')]

    # If there are no files, exit the function
    if not files:
        print("No files found in the Downloads folder.")
        return
    
    # Find the most recent file
    most_recent_file = max(files, key=os.path.getctime)

    return most_recent_file

def move_and_rename_file(destination_folder:str, file:str, new_name:str):
    destination = os.path.expanduser(destination_folder)

    # Extract file extension of the most recent file
    file_extension = os.path.splitext(file)[1]
    
    # Define the new file name with the same extension
    new_file_name = new_name + file_extension

    # Full path for the new renamed file in the destination folder
    new_file_path = os.path.join(destination, new_file_name)

    # Move and rename the file
    shutil.move(file, new_file_path)
    
    print(f"File moved and renamed to: {new_file_path}")

def move_download(new_name:str):
    destination_folder = "~/code/playground/crawler_unternehmensregister/data"
    file = get_most_recent_download()
    move_and_rename_file(destination_folder=destination_folder, file=file, new_name=new_name)