import os

PARENT_DIR = os.path.join(os.getcwd(), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_02.txt")

POINTS = {"X": 1, "Y": 2, "Z": 3}
WIN = {"A": "Y", "B": "Z", "C": "X"}
DRAW = {"A": "X", "B": "Y", "C": "Z"}
LOSE = {"A": "Z", "B": "X", "C": "Y"}

PART2 = {"X": (LOSE, 0), "Z": (WIN, 6), "Y": (DRAW, 3)}


def solve_day2(part_two=False):
    with open(INPUT, encoding="utf-8") as text:
        rounds = [game.split() for game in text.readlines()]
    # rounds = [["A", "Y"], ["B", "X"], ["C", "Z"]]
    total = 0
    if part_two:
        for hands in rounds:
            total += PART2[hands[1]][1] + POINTS[PART2[hands[1]][0][hands[0]]]
    else:
        for hands in rounds:
            if WIN[hands[0]] == hands[1]:
                total += POINTS[hands[1]] + 6
            elif DRAW[hands[0]] == hands[1]:
                total += POINTS[hands[1]] + 3
            else:
                total += POINTS[hands[1]]
    return total


if __name__ == "__main__":

    print(f"The answer to part 1 is: {solve_day2()}")
    print(f"The answer to part 2 is: {solve_day2(part_two=True)}")
