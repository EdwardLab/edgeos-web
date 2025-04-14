import os

def main(args):
    if not args:
        print("Usage: mkdir [-p] <dir>")
        return
    recursive = False
    paths = []
    for arg in args:
        if arg == "-p":
            recursive = True
        else:
            paths.append(arg)
    for path in paths:
        try:
            if recursive:
                os.makedirs(path, exist_ok=True)
            else:
                os.mkdir(path)
        except Exception as e:
            print(f"mkdir: {path}: {e}")
