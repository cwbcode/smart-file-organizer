#!/usr/bin/env python3
import argparse, re, shutil
from pathlib import Path
from datetime import datetime

def parse_command(text: str):
    intent = next((w for w in ["move", "copy", "delete", "rename"] if w in text), "move")
    dest = None
    m = re.search(r"\bto\s+(.+)", text)
    if m: dest = Path(m.group(1).strip().strip('"')).expanduser()
    recursive = "recurs" in text
    rename = "by date" in text
    return intent, dest, recursive, rename

def organize(command: str, cwd: Path, commit=False):
    intent, dest, recursive, rename = parse_command(command)
    cwd = cwd.expanduser()
    files = list(cwd.rglob("*") if recursive else cwd.glob("*"))
    files = [f for f in files if f.is_file()]
    if not files: 
        print("No files found.")
        return
    if intent in ("move", "copy") and dest:
        dest.mkdir(parents=True, exist_ok=True)
    for f in files:
        new_name = f.name
        if rename:
            date = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d")
            new_name = f"{date}_{f.name}"
        target = dest / new_name if dest else f.with_name(new_name)
        if intent == "delete":
            print(f"[plan] delete {f}")
            if commit: f.unlink()
        elif intent == "rename":
            print(f"[plan] rename {f.name} -> {new_name}")
            if commit: f.rename(target)
        elif intent == "move":
            print(f"[plan] move {f} -> {target}")
            if commit: shutil.move(f, target)
        elif intent == "copy":
            print(f"[plan] copy {f} -> {target}")
            if commit: shutil.copy2(f, target)
    if not commit:
        print("\n(dry run — add --commit to apply)")

def main():
    ap = argparse.ArgumentParser(description="Smart File Organizer")
    ap.add_argument("command", help="e.g. 'move all pngs to C:\\Pictures by date'")
    ap.add_argument("--cwd", default=".", help="working directory (default: .)")
    ap.add_argument("--commit", action="store_true", help="apply changes")
    args = ap.parse_args()
    organize(args.command, Path(args.cwd), commit=args.commit)

if __name__ == "__main__":
    main()
