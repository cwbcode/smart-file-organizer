# 🧠 Smart File Organizer (SFO)

A natural-language command-line tool that performs file operations — **move**, **copy**, **rename**, or **delete** — safely and intelligently.

> Example:  
> `sfo "move all screenshots to ~/Pictures/screenshots by date recursively"`

---

## ✨ Features
- 🗂️ Understands natural-language commands  
  > “move pdfs from Downloads to Documents”  
- 🧪 **Dry-run by default** — shows what would happen before making changes  
- 🔁 Supports recursive folder traversal  
- 🕒 Optional date-based renaming (`by date` or `by datetime`)  
- ⚙️ Works cross-platform (Windows, macOS, Linux)

---

## 🚀 Quick Start

### 1) Clone & setup (Windows/PowerShell)

    git clone https://github.com/cwbcode/smart-file-organizer.git
    cd smart-file-organizer
    python -m venv .venv
    .venv\Scripts\activate
    python -m pip install -e .

### 2) Example usage

    # Dry-run (default)
    sfo "move all screenshots to .\shots by date recursively"

    # Actually apply the changes
    sfo "move all screenshots to .\shots by date recursively" --commit

---

## 🧩 How it works
1. Parses natural-language text to infer:
   - Intent (`move`, `copy`, `delete`, `rename`)
   - Source and destination paths
   - File patterns (`png`, `pdfs`, etc.)
   - Rename options (`by date`, `slug`, `prefix`, etc.)
2. Prints a plan (dry-run) so you can verify actions.
3. Executes the operations only when `--commit` is supplied.

---

## 🧰 Development

Run locally without installing:

    python src\organizer.py "move all pngs to .\sorted by date"

Run as a CLI after install:

    sfo "move all pngs to .\sorted by date"

---

## 🧼 Safety Notes
- Dry-run mode prevents accidents — review output first.
- Always test commands in a temp directory before using on real data.

---

## 📄 License
MIT License © 2025 [cwbcode](https://github.com/cwbcode)
