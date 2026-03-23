import sys
import re

def extract_blocks(text):
    pattern = r"'''(.*?)'''"
    return re.findall(pattern, text, re.DOTALL)

def main():
    # 標準入力から全文を読み込む
    text = sys.stdin.read()
    
    blocks = extract_blocks(text)

    for i, b in enumerate(blocks, 1):
        print(f"Block {i}:")
        print(b)
        print("------")

if __name__ == "__main__":
    main()
