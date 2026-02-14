import ctypes
import datetime

DESCRIPTION = "Shows how long the system has been running."
USAGE = "uptime"
ALIASES = ["up", "runtime"]

def run(args):
    try:
        millis = ctypes.windll.kernel32.GetTickCount64()
        
        uptime_delta = datetime.timedelta(milliseconds=millis)
        
        days = uptime_delta.days
        hours, remainder = divmod(uptime_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print("\033[94mSystem Uptime:\033[0m")
        if days > 0:
            print(f"  {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
        else:
            print(f"  {hours} hours, {minutes} minutes, {seconds} seconds")
            
    except Exception as e:
        print(f"\033[91mError retrieving uptime:\033[0m {e}")
