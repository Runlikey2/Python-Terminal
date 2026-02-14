import os

DESCRIPTION = "Changes the current directory."
USAGE       = "cd foldername"
ALIASES = ["cs"]

def run(args):
    target = [a[0:] for a in args if a.startswith("")]
    
    if not target:
        print("Usage: cd foldername")
        return

    try:
        os.chdir(target[0])
        print(f"Moved to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: Folder '{target[0]}' not found.")