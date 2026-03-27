import sys
import re

def extract_blocks(text):
    pattern = r"```(.*?)```"
    return re.findall(pattern, text, re.DOTALL)

def main():
    text = sys.stdin.read()
    blocks = extract_blocks(text)

    for i, b in enumerate(blocks, 1):
        lines = b.splitlines()
        trimmed = "\n".join(lines[1:])

        print(f"Block {i}:")
        print(trimmed)
        print("------")

if __name__ == "__main__":
    main()
