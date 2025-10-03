import os
import shutil
from datetime import datetime

LOG_FILE = "organization_log.txt"

def handle_duplicate(target_path):

def organize_by_type(folder):
    file_types = {
        "Images": [".jpg",".jpeg",".png",".gif"],
        "Videos": [".mp4",".avi",".mov",".mkv"],
        "Documents": [".pdf",".docx",".txt",".pptx"],
        "Music": [".mp3",".wav"],
        "Archives": [".zip",".rar"]
    }
    
    with open(LOG_FILE,"w",encoding="utf-8") as f:
        f.write(f"--- Organization Log ({datetime.now()}) ---\n")

    for filename in os.listdir(folder):
        filepath = os.path.join(folder,filename)
        if os.path.isfile(filepath):
            try:
                _ , ext = os.path.splitext(filename)
                ext = ext.lower()
                moved = False

                for category,extensions in file_types.items():
                    if ext in extensions:
                        target_folder = os.path.join(folder,category)
                        os.makedirs(target_folder,exist_ok=True)

                        new_path = handle_duplicates(os.path.join(target_folder,filename))
                        shutil.move(filepath,new_path)

                        write_log(f"{filepath} -> {new_path}")
                        moved = True
                        break

                if not moved:
                    # file for which we dont know extension it goes to "others"
                    target_folder = os.path.join(folder,"Others")
                    os.makedirs(target_folder,exist_ok=True)
                    new_path = handle_duplicates(os.path.join(target_folder,filename))
                    shutil.move(filepath,new_path)
                    write_log(f"{filepath} -> {new_path}")

            except Exception as e:
                write_log(f"ERROR: Could not move {filepath} → {e}")

