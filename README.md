## FileOrganizer

Organize files in a directory by analyzing file headers and sorting them into folders by type. Uses the `python-magic` library and Python 3.10+ pattern matching.

---

### 🔧 Features
- Classifies files using actual content (via `libmagic`) instead of relying on extensions
- Uses Python 3.10 `match` statements for clarity and extensibility
- Automatically creates folders for:
  - Archives
  - Images
  - Scripts
  - Documents
  - Certificates
  - Miscellaneous types

---

### 🚀 Requirements
- Python >= 3.10
- libmagic (see below for installation help)

Install Python requirements:
```bash
pip install -r requirements.txt
```

If you encounter a `libmagic` error on macOS:
```bash
brew install libmagic
```

---

### 📂 Usage
Run the script with a folder path:
```bash
python file_organizer.py -fp /path/to/folder
```

You will be prompted if the path is invalid or risky (like your OS root).

---

### 📦 Packaging
To install as a package:
```bash
pip install .
```

---

### 🗃️ .gitignore
Common Python ignore rules have been included:
- `__pycache__/`
- `*.pyc`
- `.DS_Store`
- `.env`

---

### 🏷 Versioning
Current version: **v1.0.0**
To tag this release:
```bash
git tag v1.0.0
git push origin v1.0.0
```

---

### 📄 License
This project is licensed under the MIT License.

---

### 🙏 Acknowledgment
This project was inspired by [Gargee Suresh’s article on Medium](https://medium.com/better-programming/how-i-use-python-to-clear-junk-on-my-laptop-6d0f6b3f36e3).

---

### 🧪 Testing
Want to add tests? A simple structure might include:
```bash
./tests
  └── test_file_organizer.py
```

---

### 💡 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

### 📬 Contact
Open an issue on [GitHub](https://github.com/jfitzpa22/FileOrganizer) for bugs or feature suggestions.
