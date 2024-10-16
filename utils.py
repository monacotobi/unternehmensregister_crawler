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




if __name__ == "__main__":
    print(get_most_recent_download())