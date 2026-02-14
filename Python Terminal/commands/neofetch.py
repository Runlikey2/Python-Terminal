import platform
import os
import subprocess
import getpass
import winreg

DESCRIPTION = "Shows all system information with a ascii art."
USAGE = "neofetch"
ALIASES = ["neofetch", "fetch"]

def get_GPU():
        try:
                cmd = ["powershell", "-Command", "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"]
                output = subprocess.check_output(cmd, shell=True).decode()
                lines = [l.strip() for l in output.split('\n') if l.strip() and l.strip() != "Name"]
                return lines[0] if lines else "Unknown GPU"
        except:
            return "Unknown GPU"
        return "Generic VGA"


def get_CPU():
    try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
            name, _ = winreg.QueryValueEx(key, "ProcessorNameString")
            winreg.CloseKey(key)
            return name.strip()
    except:
        return platform.processor()


def run(args):

    G = "\033[92m" 
    B = "\033[94m" 
    P = "\033[95m" 
    C = "\033[96m" 
    Y = "\033[93m"
    R = "\033[0m"  

    art = [
        f"            {G}.PLTJ.{R}       ",
        f"           {G}<><><><>{R}      ",
        f"   {G}KKSSV' 4KKK  KKKL.'VSSKK{R}",
        f"   {G}KKV' 4KKKKK  KKKKAL 'VKK{R}",
        f"   {G}V'   'VKKKK  KKKKV'  'V{R}",
        f"   {G}.4MA.  'VKK  KKV' .4Mb.{R}",
        f" {P}<QDD ++++++++++++++++ GFD>{R}",
        f"   {B}'VD KKKKKKK  KKKKKKKK FV{R}",
        f"   {B} VKXXXX. '4  K .'KKKKKV {R}",
        f"   {B}  'VK' .4KK  KKA. 'KV'  {R}",
        f"   {B}  A. .4KKKK  KKKKA. .4   {R}",
        f"   {B}KKA.  'KKKK  KKKKK'  .4KK {R}",
        f"           {G}<><><><>{R}      ",
        f"            {G}'MKKM'{R}       "
    ]

    # System Information
    username = getpass.getuser()
    hostname = platform.node()
    
    info = [
        f"{Y}{username}{R}@{Y}{hostname}{R}",
        f"{Y}----------{R}",
        f"{G}OS:{R}      {platform.system()} {platform.release()}",
        f"{G}HOST:{R}    {platform.node()}",
        f"{G} KERNEL:{R}  {platform.version().split()[0]}",
        f"{G} USER:{R}    {os.getlogin()}",
        f"{G}PYTHON:{R}  {platform.python_version()}",
        f"{G}CPU:{R}     {get_CPU()}",
        f"{G}GPU{R}      {get_GPU():}",
        "",
        f"\033[40m  \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m  {R}",
        f"\033[100m  \033[101m  \033[102m  \033[103m  \033[104m  \033[105m  \033[106m  \033[107m  {R}"
    ]

    print("") 
    
    max_lines = max(len(art), len(info))
    for i in range(max_lines):
        left = art[i] if i < len(art) else " " * 25
        right = info[i] if i < len(info) else ""
        print(f"  {left}   {right}")

    print("") 