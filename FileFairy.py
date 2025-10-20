import os
import shutil
import json
from datetime import datetime

CATEGORIES ={
    "Images": [".jpg",".jpeg",".png",".gif"],
    "Videos": [".mp4",".avi",".mov"],
    "Documents": [".pdf",".docx",".txt"],
    "Music": [".mp3",".wav"],
    "Archives": [".zip",".rar"],
    "Others": []
}

LOG_FILE = "file_fairy_log.json"
UNDO_FILE = "undo.json"

# functions 
def save_json(data,file):
    with open(file,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)
''' while storing each element in new line and indent to make json pretty json.dumps({"a": {"b": {"c": 3}}}, indent=4)
{
    "a": {
        "b": {
            "c": 3
        }
    }
}
'''
def load_json(file):
    if os.path.exists(file):
        with open(file,"r",encoding='utf-8') as f:
            return json.load(f)
    return {}
def handle_duplicates(path):
    fp,ext = os.path.splitext(path)
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        new_path = f"{fp}({counter}){ext}"
        counter += 1
    return new_path

  
def organize_by_type(folder_path):
    log = {}
    undo = {}

    log["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log["mode"] = "type"
# try to keep history of these logs with time for future or time thookiru
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
                        log[file_name] = {"from": file_path,"to": f"ERROR: {str(e)}"}    #str just to be sure nothing goes wrong
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

def organize_by_date(folder_path):
    log = {}
    undo = {}

    log["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log["mode"] = "date"

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file_name)
        if os.path.isfile(file_path):
            timestamp = os.path.getmtime(file_path)
            date = datetime.datetime.fromtimestamp(timestamp)
            year = str(date.year)
            month = date.strftime("%B")

            target_dir = os.path.join(folder_path,year,month)
            os.makedirs(target_dir,exist_ok=True)

            new_path = os.path.join(target_dir,file_name)
            shutil.move(file_path,new_path)

            log[file_name] = {"from": file_path,"to": new_path}
            undo[new_path] = file_path
            
    save_json(log,LOG_FILE)
    save_json(undo,UNDO_FILE)
    print("✅ Organized by date (Year/Month).")
def organize_by_size(folder_path):
    log = {}
    undo = {}
    
    log["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log["mode"] = "size"
    



def undo_last_operation():
    undo = load_json(UNDO_FILE)
    if not undo:
        print("No operation to undo!")
        return

    log = load_json(LOG_FILE)

    for new_path, original_path in undo.items():
        if os.path.exists(new_path):
            os.makedirs(os.path.dirname(original_path), exist_ok=True)   #folderpath=os.path.dirname("/home/user/project/sha.txt")-->/home/user/project

            try:
                shutil.move(new_path, original_path)
                log[f"UNDO-{os.path.basename(new_path)}"] = {                
                    "from": new_path, "to": original_path                 #os.path.basename("/home/user/project/sha.txt")-->sha.txt
                } 
            except Exception as e:
                log[f"UNDO-{os.path.basename(new_path)}"] = {
                    "from": new_path, "to": f"ERROR: {str(e)}"
                }

    os.remove(UNDO_FILE)
    save_json(log,LOG_FILE)
    print("Undo completed.")

def show_log_report():
    log = load_json(LOG_FILE)
    if not log:
        print("No logs available")
        return
    print("\n📜 File Organizer Log:")
    for file,paths in log.items():
        if isinstance(paths,dict):                                   #x = 10   print(isinstance(x, int))  # Output: True
            print(f" - {file}: {paths['from']} → {paths['to']}")
        else:
            print(f" -{file}: {paths}")
def menu():
    while True:
        print("\n Advanced File Organizer")
        print("1. Organize by File Type")
        print("2. Organize by Date")
        print("3. Organize by Size")
        print("4. Undo Last Operation")
        print("5. Show Log Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter folder path: ")
            organize_by_type(path)
        elif choice == "2":
            path = input("Enter folder path: ")
            organize_by_date(path)
        elif choice == "3":
            path = input("Enter folder path: ")
            organize_by_size(path)
        elif choice == "4":
            undo_last_operation()
        elif choice == "5":
            show_log()
        elif choice == "6":
            print(" Exiting Advanced File Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# ------------------------------
# Run Program
# ------------------------------
if __name__ == "__main__":
    menu()
