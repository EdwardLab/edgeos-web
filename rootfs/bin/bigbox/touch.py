import os

def main(args):
    if not args:
        print("Usage: touch <file>")
        return
    for name in args:
        with open(name, "a"):
            os.utime(name, None)
