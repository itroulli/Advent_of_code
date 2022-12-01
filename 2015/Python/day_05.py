""" --- Day 5: Doesn't He Have Intern-Elves For This? --- """
import os
import sys
from itertools import groupby


PARENT_DIR = os.path.join(os.cwd(), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_05.txt")


def rules_through(funcs, x):
    return (f(x) for f in funcs)


def read_input(input_file):
    with open(input_file) as text:
        input_strings = text.readlines()
        return input_strings


def three_vowels(seq):
    cnt = 0
    for ch in seq:
        if ch in ("a", "e", "i", "o", "u"):
            cnt += 1
            if cnt == 3:
                return True
    return False


def consecutive_letters(seq):
    return any((len(list(vals)) > 1) for (char, vals) in groupby(seq))


def not_unwanted_strings(seq):
    for i in range(len(seq) - 1):
        if seq[i : i + 2] in ["ab", "cd", "pq", "xy"]:
            return False
    return True


def pair_twice(seq):
    for i in range(len(seq) - 3):
        if seq[i : i + 2] in seq[i + 2 :]:
            return True
    return False


def between_repeated(seq):
    for i in range(len(seq) - 2):
        if seq[i] == seq[i + 2]:
            return True
    return False


PART1_RULES = [three_vowels, consecutive_letters, not_unwanted_strings]
PART2_RULES = [pair_twice, between_repeated]


def find_nice(input_strings, part_two=False):
    if part_two:
        return sum([all(rules_through(PART2_RULES, seq)) for seq in input_strings])
    else:
        return sum([all(rules_through(PART1_RULES, seq)) for seq in input_strings])


if __name__ == "__main__":
    input_strings = read_input("inputs/day_05.txt")
    print(f"The answer for part 1 is: {find_nice(input_strings)}")
    print(f"The answer for part 2 is: {find_nice(input_strings, part_two=True)}")
