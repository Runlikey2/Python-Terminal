import os
import msvcrt
import sys

DESCRIPTION = "A simple text editor."
USAGE       = "edit -filename"
ALIASES     = ["edit", "editor"]

def run(args):
    target = [a[1:] for a in args if a.startswith("-")]
    if not target:
        print("Usage: edit -filename")
        return
    
    filename = target[0]

    if "." not in filename:
        filename += ".txt"

    content = []
    current_line = ""
    menu_active = False
    menu_selection = 0 # 0 = Save, 1 = Discard
    

    HEADER_BG = "\033[44m"
    SELECT_BG = "\033[42m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    if os.path.exists(filename):
        choice = input(f"File '{filename}' exists. Load content? (y/n): ").lower()
        if choice == 'y':
            try:
                with open(filename, 'r') as f:
                    content = [line.rstrip('\n') for line in f.readlines()]
            except Exception as e:
                print(f"Error loading file: {e}")
                return

    while True:
        print("\033[H\033[J", end="")
        width = 80 
        try: width = os.get_terminal_size().columns
        except: pass

        if menu_active:
            save_tab = f"{SELECT_BG if menu_selection == 0 else ''} [SAVE] {RESET}{HEADER_BG}"
            quit_tab = f"{SELECT_BG if menu_selection == 1 else ''} [DISCARD] {RESET}{HEADER_BG}"
            header_text = f"  {save_tab}  {quit_tab}  "
            print(f"{HEADER_BG}{WHITE}{header_text.ljust(width + 15)}{RESET}") 
        else:
            print(f"{HEADER_BG}{WHITE}{'Python Text Editor'.center(width)}{RESET}")

        for i, line in enumerate(content):
            print(f"{i+1}: {line}")

        print(f"{len(content)+1}: {current_line}", end="", flush=True)

        char = msvcrt.getch()

        if char in [b'\x00', b'\xe0']:
            key = msvcrt.getch()
            if key == b'H': 
                menu_active = True
            elif key == b'P': 
                menu_active = False
            elif key == b'K' and menu_active: 
                menu_selection = 0
            elif key == b'M' and menu_active: 
                menu_selection = 1

        elif char == b'\r':
            if menu_active:
                if menu_selection == 0: 
                    with open(filename, 'w') as f:
                        f.write("\n".join(content + ([current_line] if current_line else [])))
                    print("\033[H\033[J", end="")
                    print("Python Terminal [Version 1.2]")
                    print("(c) Python Corporation. All rights reserved.")
                    print(f"\033[92mFile '{filename}' saved successfully.\033[0m")
                    break
                else:
                   print("\033[H\033[J", end="")
                   print("Python Terminal [Version 1.2]")
                   print("(c) Python Corporation. All rights reserved.")
                   print("\033[93mChanges discarded.\033[0m")
                   break
            else:
                content.append(current_line)
                current_line = ""

        elif char == b'\x08':
            current_line = current_line[:-1]

        else:
            try:
                current_line += char.decode('utf-8')
            except: pass