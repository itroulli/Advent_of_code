import os
from itertools import groupby

PARENT_DIR = os.path.join(os.getcwd(), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_01.txt")


def solve_day1(part_two=False):
    with open(INPUT, encoding="utf-8") as text:
        input_text = text.readlines()

    elves = [list(y) for x, y in groupby(input_text, lambda z: z == "\n") if not x]
    elves_inv = [sum(map(int, elf)) for elf in elves]
    if part_two:
        elves_inv.sort(reverse=True)
        print(f"Answer to part 2: {sum(elves_inv[:3])}")
    else:
        print(f"Answer to part 1: {max(elves_inv)}")


if __name__ == "__main__":
    solve_day1()
    solve_day1(part_two=True)
