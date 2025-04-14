async def main(args):
    print("[test] Starting interactive input")
    name = await input("Your name: ")
    print("Hello", name)
