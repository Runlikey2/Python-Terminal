import os

DESCRIPTION = "Clears the terminal screen."
USAGE = "clear"
ALIASES = ["cls", "clear"]

def run(args):
    print("\033[H\033[J", end="")
    print("Python Terminal [Version 1.2]")
    print("(c) Python Corporation. All rights reserved.")