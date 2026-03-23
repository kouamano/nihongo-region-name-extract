import sys

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '/': '/',  # / は同一文字対応
}

opening = set(pairs.values())
closing = set(pairs.keys())

def is_valid_line(line):
    stack = []
    found_bracket = False  # 括弧が存在するか確認

    for ch in line:
        if ch in opening:
            stack.append(ch)
            found_bracket = True
        elif ch in closing:
            if not stack:
                return False
            if stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return False

    # 括弧が少なくとも1つあり、かつ完全に対応している
    return found_bracket and len(stack) == 0

def main():
    for line in sys.stdin:
        line = line.rstrip("\n")
        if is_valid_line(line):
            print(line)

if __name__ == "__main__":
    main()
