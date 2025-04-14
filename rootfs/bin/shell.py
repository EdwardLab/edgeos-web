import os
import js
import importlib.util

print("[BOOTLOADER] EdgeOS WEB, kernel 0.27.5")
print(f"[BOOT] Python {os.sys.version}")

def print_motd():
    motd_path = "/etc/motd"
    if os.path.isfile(motd_path):
        try:
            with open(motd_path) as f:
                print(f.read().strip())
        except Exception as e:
            print(f"[SHELL] failed to read motd or not found: {e}")

print_motd()



# ======== Filesystem Initialization ========
def init_filesystem():
    os.makedirs("/home/user", exist_ok=True)
    os.chdir("/home/user")

init_filesystem()

# ======== Async Safe Input Setup ========

async def safe_input(prompt=""):
    try:
        if hasattr(js, "terminal") and hasattr(js.terminal, "input"):
            return await js.terminal.input(prompt)
        else:
            result = js.eval(f'prompt({prompt!r})') or ""
            return str(result)
    except Exception as e:
        raise RuntimeError(f"[input] failed: {e}")

__builtins__.input = safe_input

# ======== PATH and Command Execution ========
COMMAND_PATHS = ["/bin/bigbox"]

async def run_command(cmd, args):
    for path in COMMAND_PATHS:
        full_path = os.path.join(path, f"{cmd}.py")
        if os.path.isfile(full_path):
            try:
                spec = importlib.util.spec_from_file_location(f"bigbox.{cmd}", full_path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, "main"):
                    result = mod.main(args)
                    if hasattr(result, "__await__"):
                        await result
                    return
                else:
                    print(f"{cmd}: no main(args) function")
                    return
            except Exception as e:
                print(f"{cmd}: error: {e}")
                return
    print(f"{cmd}: command not found")

# ======== Shell Main Loop ========
async def shell():
    print("Welcome to EdgeOS Web Shell — type 'help'")
    while True:
        try:
            line = await input(f"{os.getcwd()} $ ")
            parts = line.strip().split()
            if not parts:
                continue
            cmd, args = parts[0], parts[1:]
            if cmd == "exit":
                print("Goodbye.")
                break
            await run_command(cmd, args)
        except Exception as e:
            print(f"[ERROR] {e}")

# ======== Launch ========
#await shell()
