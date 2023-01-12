import math
import os
from typing import List, Tuple
from operator import add

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_09.txt")


def read_input(fname: str) -> List[Tuple[str, int]]:
    """Read the list of directions and steps for the head to move and
    return it as a list of lists of strings"""
    with open(fname, "r", encoding="utf-8") as src_fh:
        lines = [line.split() for line in src_fh.read().splitlines()]
    lines = [(line[0], int(line[1])) for line in lines]
    return lines


def distance(p0: Tuple, p1: Tuple) -> float:
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


def solve_day9(part_two=False):
    STEPS = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
    lines = read_input(INPUT)
    if not part_two:
        visited_by_tail = [(0, 0)]
        current_H = (0, 0)
        current_T = (0, 0)
        for direction in lines:
            for _ in range(direction[1]):
                prev_H = current_H
                current_H = tuple(map(add, current_H, STEPS[direction[0]]))
                if distance(current_H, current_T) >= 2:
                    current_T = prev_H
                    visited_by_tail.append(current_T)
        print(f"The answer to part 1 is: {len(set(visited_by_tail))}")


if __name__ == "__main__":
    solve_day9()
