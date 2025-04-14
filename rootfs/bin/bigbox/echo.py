def main(args):
    if not args:
        print()
        return
    if ">" in args:
        idx = args.index(">")
        text = " ".join(args[:idx])
        filename = args[idx + 1]
        with open(filename, "w") as f:
            f.write(text + "\n")
    else:
        print(" ".join(args))
