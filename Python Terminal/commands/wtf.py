import os
import importlib

DESCRIPTION = "wtf is [command]."
USAGE = "wtf is [command]"
ALIASES = ["wtf"]

def run(args):
    commands_dir = "commands"
    
    if len(args) >= 2 and args[0].lower() == "is":
        target_cmd = args[1]
    elif len(args) == 1:
        target_cmd = args[0]
    else:
        target_cmd = None

    files = [f[:-3] for f in os.listdir(commands_dir) 
             if f.endswith(".py") and f != "__init__.py"]

    if target_cmd:
        if target_cmd not in files:
            print(f"I don't know what '{target_cmd}' is.")
            return
        files = [target_cmd]

    for cmd in sorted(files):
        try:
            module = importlib.import_module(f"{commands_dir}.{cmd}")
            importlib.reload(module)

            desc = getattr(module, "DESCRIPTION", "No description.")
            
            if target_cmd:
                print(f"Description: {desc}")
                
        except Exception as e:
            print(f"{cmd:<15} | Error loading command: {e}")