import os

def main(args):
    # Define default home directory
    home_dir = "/home/user"

    # No argument → go to $HOME
    if not args:
        target = home_dir
    else:
        target = args[0]
        # Expand ~ to home
        if target == "~":
            target = home_dir
        elif target.startswith("~/"):
            target = os.path.join(home_dir, target[2:])

    # Resolve absolute path
    path = os.path.abspath(target)

    if os.path.isdir(path):
        os.chdir(path)
    else:
        print(f"cd: no such directory: {target}")
