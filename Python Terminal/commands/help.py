import os
import importlib

DESCRIPTION = "Shows all available commands and their aliases."
USAGE = "help"
ALIASES = ["cmds", "info", "commands"]

def run(args):
    commands_dir = "commands"
    
    files = [f[:-3] for f in os.listdir(commands_dir) 
             if f.endswith(".py") and f != "__init__.py"]
    

    print(f"\n{'COMMAND':<15} | {'ALIASES':<20} | {'DESCRIPTION'}")
    print("-" * 60)

    for cmd in sorted(files):
        try:
            module = importlib.import_module(f"{commands_dir}.{cmd}")
            importlib.reload(module)
            
            if getattr(module, "HIDDEN", False):
                    continue

            aliases_list = getattr(module, "ALIASES", [])
            alias_str = " ".join(aliases_list) if aliases_list else ""

            desc = getattr(module, "DESCRIPTION", "No description.")
            aliases = ", ".join(getattr(module, "ALIASES", []))
            
            print(f"{cmd:<15} | {aliases:<20} | {desc}")
        except Exception:
            print(f"{cmd:<15} | {'Error loading command':<20} | ---")
    print("") 