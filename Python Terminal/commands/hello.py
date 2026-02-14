DESCRIPTION = "Greets the user or a specific name."
USAGE = "hello [name]"
ALIASES = ["hello"]

def run(args):

    filtered_args = [a[1:] for a in args if a.startswith("-")]

    if filtered_args:
        print(f"Hello, {' '.join(filtered_args)}!")
    else:
        print("Hello, World!")