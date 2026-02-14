import os
import subprocess
import platform

DESCRIPTION = "Opens a file in its default editor or executes a program."
USAGE       = "open -filename.ext"
ALIASES     = ["run", "start", "launch"]

G = "\033[92m" 
R = "\033[0m"  
RED = "\033[91m" 

def run(args):
    target = [a[1:] for a in args if a.startswith("-")]
    
    if not target:
        print(f"{RED}Error: Specify a file using -filename{R}")
        return

    file_to_open = target[0]

    if not os.path.exists(file_to_open):
        print(f"{RED}Error: File '{file_to_open}' not found.{R}")
        return

    try:
        print(f"{G}Opening {file_to_open}...{R}")

        system_name = platform.system()
        
        if system_name == "Windows":
            os.startfile(file_to_open)
        elif system_name == "Darwin":
            subprocess.call(('open', file_to_open))
        else: 
            subprocess.call(('xdg-open', file_to_open))
            
    except Exception as e:
        print(f"{RED}Failed to open file: {e}{R}")
