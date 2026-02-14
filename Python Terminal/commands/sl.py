import time
import sys

DESCRIPTION = "Changes the current directory."
USAGE = "cd foldername"
ALIASES = ["sl"]

def run(args):
    train = [
        "      ====        ________                ___________",
        "  _D _|  L_  .-|\"\"\"\"\"\"\"\"\"\"|-.      .-| \"\"\"\"\"\"\"\"\"\" |-. ",
        " /|________| |____________| |      | |____________| |",
        " |_________| |____________| |      | |____________| |",
        " |_|_| |_|_| |_|_|____|_|_|        |_|_|____|_|_|  ",
    ]
    for i in range(50, -10, -1):
        sys.stdout.write("\033[H\033[J")
        for line in train:
            print(" " * i + line)
        time.sleep(0.05)
        sys.stdout.write("\033[H\033[J")
        sys.stdout.write("Python Terminal [Version 1.2]\n")
        sys.stdout.write("(c) Python Corporation. All rights reserved.\n")