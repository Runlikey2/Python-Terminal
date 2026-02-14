import platform
import os

DESCRIPTION = "Shows system information."
USAGE = "sys"
ALIASES = ["sysinfo"]

def run(args):
    G = "\033[92m"
    R = "\033[0m"
    
    print(f"{G}OS:{R} {platform.system()} {platform.release()}")
    print(f"{G}Processor:{R} {platform.processor()}")
    print(f"{G}Current User:{R} {os.getlogin()}")
    print(f"{G}Python Version:{R} {platform.python_version()}")