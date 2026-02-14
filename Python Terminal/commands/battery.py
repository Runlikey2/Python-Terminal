import ctypes
from ctypes import wintypes

DESCRIPTION = "Displays battery percentage and power status."
USAGE = "battery"
ALIASES = ["pwr", "power", "bat"]

class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]

def run(args):
    status = SYSTEM_POWER_STATUS()
    
    if ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status)):

        power_source = "Plugged In (AC)" if status.ACLineStatus == 1 else "Battery"
        color = "\033[92m" if status.ACLineStatus == 1 else "\033[93m"

        percent = status.BatteryLifePercent

        print(f"\033[1m--- Power Status ---\033[0m")
        
        if percent == 255 or percent < 0:
            print("Battery: Not Detected (Desktop PC?)")
        else:
            bar_length = 20
            filled = int(percent / 100 * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            print(f"Source:  {color}{power_source}\033[0m")
            print(f"Level:   [{bar}] {percent}%")
            
            if status.ACLineStatus == 0:
                seconds = status.BatteryLifeTime
                if seconds != -1 and seconds != 4294967295:
                    hours = seconds // 3600
                    mins = (seconds % 3600) // 60
                    print(f"Time:    ~{hours}h {mins}m remaining")
    else:
        print("\033[91mError:\033[0m Could not retrieve power status.")
