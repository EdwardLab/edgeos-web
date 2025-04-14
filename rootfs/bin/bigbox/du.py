import os

def format_bytes(size, base=1024):
    units = ['B', 'K', 'M', 'G', 'T']
    i = 0
    while size >= base and i < len(units) - 1:
        size /= base
        i += 1
    return f"{size:.1f}{units[i]}"

def get_size(path):
    total = 0
    if os.path.isfile(path):
        total += os.path.getsize(path)
    else:
        for root, dirs, files in os.walk(path):
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    total += os.path.getsize(fp)
                except:
                    pass
    return total

async def main(args):
    show_all = "-a" in args
    human = "-h" in args
    summary_only = "-s" in args or not show_all

    # get target path
    paths = [arg for arg in args if not arg.startswith("-")]
    target = paths[0] if paths else "."

    if not os.path.exists(target):
        print(f"du: cannot access '{target}': No such file or directory")
        return

    def display(size, path):
        if human:
            print(f"{format_bytes(size):>8} {path}")
        else:
            print(f"{size:>8} {path}")

    if summary_only:
        size = get_size(target)
        display(size, target)
    else:
        if os.path.isfile(target):
            display(os.path.getsize(target), target)
        else:
            for root, dirs, files in os.walk(target):
                for d in dirs:
                    full_path = os.path.join(root, d)
                    size = get_size(full_path)
                    display(size, full_path)
                for f in files:
                    full_path = os.path.join(root, f)
                    try:
                        size = os.path.getsize(full_path)
                        display(size, full_path)
                    except:
                        continue
