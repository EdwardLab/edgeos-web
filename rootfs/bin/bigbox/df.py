import js

def format_bytes(size, base=1024):
    if base == 1000:
        unit = ['B', 'K', 'M', 'G', 'T']
    else:
        unit = ['B', 'Ki', 'Mi', 'Gi', 'Ti']
    i = 0
    while size >= base and i < len(unit) - 1:
        size /= base
        i += 1
    return f"{size:.1f}{unit[i]}"

async def main(args):
    human = "-h" in args
    human_1000 = "-H" in args
    show_type = "-T" in args
    all_entries = "-a" in args

    try:
        estimate = await js.navigator.storage.estimate()
        used = estimate.usage or 0
        quota = estimate.quota or 0
        avail = quota - used
        percent = int((used / quota) * 100) if quota else 0

        base = 1000 if human_1000 else 1024
        formatter = format_bytes if human or human_1000 else lambda x, base=None: str(int(x))

        # header
        headers = ["Filesystem"]
        if show_type:
            headers.append("Type")
        headers += ["Size", "Used", "Avail", "Use%", "Mounted on"]
        print(" ".join(f"{h:<12}" for h in headers))

        # row
        row = ["/home/user"]
        if show_type:
            row.append("idbfs")
        row += [
            formatter(quota, base).rjust(10),
            formatter(used, base).rjust(10),
            formatter(avail, base).rjust(10),
            f"{percent:>4}%",
            "/mnt/rootfs"
        ]
        print(" ".join(str(r).ljust(12) for r in row))

        # fake extra mount if -a
        if all_entries:
            print("none         tmpfs        0           0           0       0%   /dev/shm")

    except Exception as e:
        print(f"df: error: {e}")
