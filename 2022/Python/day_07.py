import os
from collections import defaultdict

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_07.txt")


def solve_day7(part_two=False):
    with open(INPUT, encoding="utf-8") as text:
        input_text = text.read().splitlines()
        lines = (command for command in input_text if command != "$ ls")
    sizes = defaultdict(int)
    path = []
    for line in lines:
        command = "d"
        if line.startswith("$ cd"):
            if (dirname := line.split(" ")[-1]) != "..":
                path.append(dirname)
            elif dirname == "/":
                path.clear()
                path.append("/")
            else:
                path.pop()
        elif str.isnumeric(size := line.split(" ")[0]):
            for i in range(len(path)):
                dirname = "/".join(path[: i + 1]).replace("//", "/")
                sizes[dirname] += int(size)
    if part_two:
        total_space = 70000000
        space_needed = 30000000
        free_now = total_space - sizes["/"]
        need_to_delete = space_needed - free_now
        answer = min([s for s in sizes.values() if s >= need_to_delete])
        print(f"The answer to part 2 is: {answer}")
    else:
        print(
            f"The answer to part 1 is: {sum([s for s in sizes.values() if s <= 100000])}"
        )


if __name__ == "__main__":
    solve_day7()
    solve_day7(part_two=True)
