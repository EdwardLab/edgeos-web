import os
import shutil

def main(args):
    if not args:
        print("Usage: rm [-r] <file/dir>")
        return

    recursive = False
    targets = []

    for arg in args:
        if arg == "-r":
            recursive = True
        else:
            targets.append(arg)

    for path in targets:
        if not os.path.exists(path):
            print(f"rm: cannot remove '{path}': No such file or directory")
            continue

        try:
            if os.path.isdir(path):
                if recursive:
                    shutil.rmtree(path)
                else:
                    print(f"rm: cannot remove '{path}': Is a directory")
            else:
                os.remove(path)
        except Exception as e:
            print(f"rm: cannot remove '{path}': {e}")
