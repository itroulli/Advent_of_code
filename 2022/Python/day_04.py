import os

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_04.txt")


def solve_day4(part_two=False):
    with open(INPUT, encoding="utf-8") as text:
        pairs = [pair.split(",") for pair in text.readlines()]
    # pairs = [
    #     ["2-4", "6-8"],
    #     ["2-3", "4-5"],
    #     ["5-7", "7-9"],
    #     ["2-8", "3-7"],
    #     ["6-6", "4-6"],
    #     ["2-6", "4-8"],
    # ]
    total = 0
    if part_two:
        for pair in pairs:
            areas = []
            for area in pair:
                x, y = tuple(map(int, area.split("-")))
                areas.append(set(range(x, y + 1)))
            if areas[0] & areas[1]:
                total += 1
    else:
        for pair in pairs:
            areas = []
            for area in pair:
                x, y = tuple(map(int, area.split("-")))
                areas.append(set(range(x, y + 1)))
            if (areas[0] & areas[1] == areas[0]) or areas[0] & areas[1] == areas[1]:
                total += 1
    return total


if __name__ == "__main__":
    print(f"Answer to part 1 is: {solve_day4()}")
    print(f"Answer to part 2 is: {solve_day4(part_two=True)}")
