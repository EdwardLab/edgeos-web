import os

def main(args):
    if not args:
        print("Usage: cat <file>")
        return
    for file in args:
        if not os.path.exists(file):
            print(f"cat: {file}: No such file")
            continue
        with open(file) as f:
            print(f.read(), end='')
