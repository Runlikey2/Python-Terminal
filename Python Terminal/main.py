import os
import importlib
import sys
import security
import getpass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
commands_dir = os.path.join(BASE_DIR, "commands")

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

def main():
    if not os.path.exists(commands_dir):
        print(f"\033[91mError: '{commands_dir}' folder not found!\033[0m")
        return
    
    print("Python Terminal [Version 1.2]")
    print("(c) Python Corporation. All rights reserved.")
    
    while True:
        user = getpass.getuser()
        prompt = f"\033[92m{user}\033[0m@\033[94mTerm\033[0m:\033[93m~\033[0m$ "
        user_input = input(prompt).strip().split()
        
        if not user_input:
            continue
        
        cmd_name = user_input[0].lower()
        args = user_input[1:]
        target_module = None
        
        try:
            files = [f for f in os.listdir(commands_dir) if f.endswith(".py") and f != "__init__.py"]
        except Exception as e:
            print(f"Error accessing commands folder: {e}")
            continue
        
        for filename in files:
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f"commands.{module_name}")
                importlib.reload(module)
                
                aliases = getattr(module, "ALIASES", [])
                if cmd_name == module_name or cmd_name in aliases:
                    target_module = module
                    break 
            except Exception:
                continue
        
        if target_module and hasattr(target_module, 'run'):
            is_protected = getattr(target_module, "PROTECTED", False)
            if is_protected:
                if security.check_login():
                    target_module.run(args)
                else:
                    pass
            else:
                target_module.run(args)
        else:
            print(f"Unknown command: '{cmd_name}'")

if __name__ == "__main__":
    main()
    input("\nProgram exited. Press Enter to close window...")