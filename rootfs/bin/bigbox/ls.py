import os
import time
import stat

def format_mode(mode):
    # Generate permission string like `-rw-r--r--`
    is_dir = "d" if stat.S_ISDIR(mode) else "-"
    perms = ""
    for who in "USR", "GRP", "OTH":
        for what in "R", "W", "X":
            perms += (mode & getattr(stat, f"S_I{what}{who}")) and what.lower() or "-"
    return is_dir + perms

def format_bytes(size):
    # Human-readable byte formatter
    for unit in ['B','K','M','G','T']:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}P"

def main(args):
    show_all = "-a" in args
    long_format = "-l" in args
    human_readable = "-h" in args
    one_per_line = "-1" in args

    # get path
    paths = [arg for arg in args if not arg.startswith("-")]
    target = paths[0] if paths else os.getcwd()

    if not os.path.exists(target):
        print(f"ls: cannot access '{target}': No such file or directory")
        return

    if os.path.isfile(target):
        print(target)
        return

    try:
        items = os.listdir(target)
        items.sort()
        if not show_all:
            items = [f for f in items if not f.startswith(".")]

        if long_format:
            for name in items:
                full_path = os.path.join(target, name)
                st = os.stat(full_path)
                mode = format_mode(st.st_mode)
                size = st.st_size
                mtime = time.strftime("%b %d %H:%M", time.localtime(st.st_mtime))
                size_str = format_bytes(size) if human_readable else str(size)
                print(f"{mode} {st.st_nlink:>2} user user {size_str:>8} {mtime} {name}")
        else:
            sep = "\n" if one_per_line else "  "
            print(sep.join(items))

    except Exception as e:
        print(f"ls: error: {e}")
