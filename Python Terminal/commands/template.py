DESCRIPTION = "Prints a hello message to the user"
USAGE       = "helloworld [-NAME]"
ALIASES = ["commandnamehere", "helloworld"]  # Commands that trigger this (check for conflicts!)
HIDDEN = False  # Set True to hide from help/wtf is commands
PROTECTED = False  # Set True to require login (see security.py)

def run(args):
    """
    Main function that executes when command is called.
    
    Args:
        args (list): Arguments passed after the command name
                     Example: "hello world" -> args = ["world"]
    """
    # If no arguments provided, just say hello
    if not args:
        print("Hello World!")
        return
    
    # Otherwise, greet the provided name/text
    text = " ".join(args)
    print(f"Hello, {text}!")
