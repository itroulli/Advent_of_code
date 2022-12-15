import os

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_03.txt")


def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)] * n)


def solve_day3(part_two=False):
    with open(INPUT, encoding="utf-8") as text:
        rucksacks = text.read().splitlines()
    # rucksacks = [
    #     "vJrwpWtwJgWrhcsFMMfFFhFp",
    #     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #     "PmmdzqPrVvPwwTWBwg",
    #     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #     "ttgJtRGJQctTZtZT",
    #     "CrZsJsPPZsGzwwsLwLmpwMDw",
    # ]
    all_common = []
    total = 0
    if part_two:
        for group in grouped(rucksacks, 3):
            badge = set(group[0]) & set(group[1]) & set(group[2])
            all_common.append(*badge)
    else:
        for rucksack in rucksacks:
            n = len(rucksack) // 2
            common_items = set(rucksack[:n]) & set(rucksack[n:])
            all_common.extend(common_items)

    for item in all_common:
        if item.islower():
            total += ord(item) - 96
        else:
            total += ord(item) - 38
    return total


if __name__ == "__main__":
    print(f"Answer to part 1 is: {solve_day3()}")
    print(f"Answer to part 2 is: {solve_day3(part_two=True)}")
