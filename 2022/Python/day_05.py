import os

from collections import defaultdict

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_05.txt")


def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)] * n)


def solve_day5(part_two=False):
    with open(INPUT, encoding="utf-8") as text:
        input_text = text.read().splitlines()

    # commands = list(map(input_text[10:], str.split(" ")))
    moves = [
        [int(move[1]), int(move[3]), int(move[5])]
        for move in (command.split(" ") for command in input_text[10:])
    ]
    stacks = defaultdict(list)
    for line in reversed(input_text[:8]):
        for i, crate in enumerate(grouped(" " + line, 4), start=1):
            if crate[2].isalpha():
                stacks[i].append(crate[2])
    if part_two:
        for move in moves:
            stacks[move[2]].extend(stacks[move[1]][-move[0] :])
            stacks[move[1]] = stacks[move[1]][: -move[0]]
    else:
        for move in moves:
            for _ in range(move[0]):
                temp = stacks[move[1]].pop()
                stacks[move[2]].append(temp)
    answer = ""
    for i in range(1, len(stacks) + 1):
        answer += stacks[i][-1]
    print(answer)


if __name__ == "__main__":
    solve_day5()
    solve_day5(part_two=True)
