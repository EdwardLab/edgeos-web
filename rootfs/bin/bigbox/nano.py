import os

async def main(args):
    if not args:
        print("Usage: nano <file>")
        return

    filename = args[0]
    if os.path.isdir(filename):
        print(f"nano: {filename}: Is a directory")
        return

    lines = []

    # Read existing file
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                lines = f.read().splitlines()
        except Exception as e:
            print(f"nano: failed to open {filename}: {e}")
            return

    print(f"Editing: {filename}")
    print("(Type lines and press Enter. Type '__SAVE__' alone to save and exit)")

    # Show current content
    if lines:
        print("--- File content ---")
        for i, line in enumerate(lines):
            print(f"{i+1:>3} | {line}")
        print("--- End ---")

    # Append lines
    while True:
        try:
            line = await input(f"{len(lines)+1:>3} | ")
            if line.strip() == "__SAVE__":
                break
            lines.append(line)
        except Exception as e:
            print(f"nano: error: {e}")
            return

    # Save
    try:
        with open(filename, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f"[nano] Saved to {filename}")
    except Exception as e:
        print(f"nano: failed to save file: {e}")
