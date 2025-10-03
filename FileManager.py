import os
import shutil
import json
from datetime import datetime

CATEGORIES = {
    "Images": [".jpg",".jpeg",".png",".gif"],
    "Videos": [".mp4",".avi",".mov"],
    "Documents": [".pdf",".docx",".txt"],
    "Music": [".mp3",".wav"],
    "Archives": [".zip",".rar"],
    "Others": []
}

LOG_FILE = "file_organizer_log.json"
UNDO_FILE = "undo.json"

# functions 
def save_json(data,file):
    with open(file,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

def load_json(file):
    if os.path.exists(file):
        with open(file,"r") as f:
            return json.load(f)
    return {}
def handle_duplicates(path):

  
def organize_by_type(folder_path):
    log = {}
    undo = {}

    log["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file_name)

        if os.path.isfile(file_path):
            # filename="document.PDF" s.path.splitext(file_name) returns the tuple ('document', '.PDF')  [1]-.PDF .lower()-.pdf
            ext = os.path.splitext(file_name)[1].lower() 
            moved = False

            for category,extensions in CATEGORIES.items():
                if ext in extensions:
                    category_folder = os.path.join(folder_path,category)
                    os.makedirs(category_folder,exist_ok=True)

                    new_path = os.path.join(category_folder,file_name)
                    new_path = handle_duplicates(new_path)  

                    try:
                        shutil.move(file_path, new_path)
                        log[file_name] = {"from": file_path,"to": new_path}
                        undo[new_path] = file_path
                    except Exception as e:
                        log[file_name] = {"from": file_path,"to": f"ERROR: {str(e)}"}
                    moved = True
                    break

            if not moved:  # goes into Others
                category_folder = os.path.join(folder_path,"Others")
                os.makedirs(category_folder,exist_ok=True)

                new_path = os.path.join(category_folder,file_name)
                new_path = handle_duplicates(new_path)

                try:
                    shutil.move(file_path,new_path)
                    log[file_name] = {"from": file_path,"to": new_path}
                    undo[new_path] = file_path
                except Exception as e:
                    log[file_name] = {"from": file_path,"to": f"ERROR: {str(e)}"}

    save_json(log,LOG_FILE)
    save_json(undo,UNDO_FILE)
