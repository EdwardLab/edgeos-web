import os

BANNER = """
BusyBox-like Utility Set — EdgeOS bigbox v0.1
Built-in commands available from: /bin/bigbox
"""

def main(args):
    print(BANNER.strip())
    
    commands_dir = "/bin/bigbox"
    if not os.path.isdir(commands_dir):
        print("bigbox: error: /bin/bigbox not found")
        return

    try:
        files = os.listdir(commands_dir)
        cmds = sorted(
            f[:-3] for f in files if f.endswith(".py") and f != "bigbox.py"
        )
        line = ""
        for i, cmd in enumerate(cmds, 1):
            line += f"{cmd:<12}"
            if i % 6 == 0 or i == len(cmds):
                print(line)
                line = ""
    except Exception as e:
        print(f"bigbox: error: {e}")
