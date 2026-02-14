import hashlib
import msvcrt
import sys

USERNAME = "admin"
PASSWORD_HASH = hashlib.sha256("Password".encode()).hexdigest()

def get_masked_input(prompt="Password: "):
    print(prompt, end='', flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        
        if char in [b'\r', b'\n']:
            print() 
            break
        elif char == b'\x08':
            if len(password) > 0:
                password = password[:-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
        else:
            password += char.decode('utf-8')
            sys.stdout.write('*')
            sys.stdout.flush()
    return password

def check_login():
    print("\033[93m--- Restricted Access ---\033[0m")
    user = input("Username: ")
    
    pwd = get_masked_input("Password: ")
    
    input_hash = hashlib.sha256(pwd.encode()).hexdigest()
    
    if user == USERNAME and input_hash == PASSWORD_HASH:
        print("\033[92mAccess Granted.\033[0m")
        return True
    else:
        print("\033[91mAccess Denied.\033[0m")
        return False