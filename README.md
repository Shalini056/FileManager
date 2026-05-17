# 📂 Advanced File Organizer

An advanced Python-based file organizer that automatically sorts files into folders based on:

- File Type
- Date
- File Size

It also supports:

- Undo Last Operation
- Duplicate File Handling
- JSON Log Reports

---

# ✨ Features

## ✅ Organize by File Type

Automatically moves files into categories like:

- Images
- Videos
- Documents
- Music
- Archives
- Others

---

## ✅ Organize by Date

Sorts files into:

```text
Year/
   Month/
      files
```

Example:

```text
2025/
   August/
   September/
```

---

## ✅ Organize by File Size

Files are categorized into:

| Category | Size |
|---|---|
| Small | 0 - 1 MB |
| Medium | 1 MB - 100 MB |
| Large | 100 MB - 1 GB |
| Huge | 1 GB+ |

---

## ✅ Undo Support

Undo the last organization operation instantly.

The program stores previous locations in:

```text
undo.json
```

---

## ✅ Duplicate File Protection

If a file with the same name already exists:

```text
photo.jpg
photo(1).jpg
photo(2).jpg
```

are automatically created.

---

## ✅ Log Reports

Every operation is stored in:

```text
file_fairy_log.json
```

with timestamps and movement history.

---

# 🛠 Technologies Used

- Python
- os module
- shutil module
- json module
- datetime module

---

# 📁 Project Structure

```text
project/
│
├── organizer.py
├── file_fairy_log.json
├── undo.json
│
├── Images/
├── Videos/
├── Documents/
├── Music/
├── Archives/
└── Others/
```

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

---

## 2. Run the Program

```bash
python organizer.py
```

---

# 📋 Menu Options

```text
1. Organize by File Type
2. Organize by Date
3. Organize by Size
4. Undo Last Operation
5. Show Log Report
6. Exit
```

---

# 📌 Example

## Before

```text
Downloads/
   photo.jpg
   song.mp3
   movie.mp4
   notes.pdf
```

## After Organize by Type

```text
Downloads/
│
├── Images/
│    └── photo.jpg
│
├── Music/
│    └── song.mp3
│
├── Videos/
│    └── movie.mp4
│
└── Documents/
     └── notes.pdf
```

---

# 🔄 Undo Example

After selecting:

```text
4. Undo Last Operation
```

All files return to their original locations.

---

# 🧠 Concepts Used

- File Handling
- Exception Handling
- Dictionaries
- JSON Handling
- Functions
- Loops
- Modular Programming
- Path Manipulation

---

# 🚀 Future Improvements

- GUI Version using Tkinter or PyQt
- Drag and Drop Support
- Automatic Real-Time Monitoring
- File Extension Customization
- Dark Mode Interface

---

# 👩‍💻 Author

Shalini M

---

# 📜 License

This project is open-source and free to use.
