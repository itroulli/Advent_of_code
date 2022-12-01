import os
from collections import Counter

PARENT_DIR = os.path.join(os.cwd(), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_01.txt")

def solve_day1(part_two=False):
    with open(INPUT) as text:
        input_text = text.read()

    if part_two:
        floor = 0
        for pos, cmd in enumerate(input_text, 1):
            if cmd == "(":
                floor += 1
            elif cmd == ")":
                floor -= 1
            if floor < 0:
                break
        print(f"Answer for part 2: {pos}")
    else:
        cnt = Counter(input_text)
        print(f"Answer for part 1: {cnt['('] - cnt[')']}")


if __name__ == "__main__":
    solve_day1()
    solve_day1(part_two=True)
