
import os

DESCRIPTION = "Lists files and folders in the current directory."
USAGE       = "dir [-all]"
ALIASES     = ["ls", "list"]

G = "\033[92m" 
C = "\033[96m" 
R = "\033[0m"  

def run(args):
    show_hidden = "-all" in args
    
    try:
        items = os.listdir('.')
        
        print(f"Directory listing for: {os.getcwd()}\n")
        
        for item in sorted(items):
            if item.startswith('.') and not show_hidden:
                continue
                
            if os.path.isdir(item):
                print(f"{G}[DIR]  {item}{R}")
            else:
                print(f"{C}[FILE] {item}{R}")
                
    except Exception as e:
        print(f"Error accessing directory: {e}")