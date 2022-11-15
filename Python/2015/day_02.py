from itertools import combinations
from operator import mul


def solve_day2():
    with open("inputs/day_02.txt", encoding="utf-8") as text:
        input_text = text.readlines()

    total = 0
    total_ribbon = 0

    for package in input_text:
        size = list(map(int, package.split("x")))
        package_areas = [2 * x * y for x, y in combinations(size, 2)]
        total += sum(package_areas) + min(package_areas) // 2

        package_ribbon = [2 * x + 2 * y for x, y in combinations(size, 2)]
        extra = 1
        for dim in size:
            extra = mul(dim, extra)
        total_ribbon += min(package_ribbon) + extra
    print(f"Answer for part 1: {total}")
    print(f"Answer for part 2: {total_ribbon}")


if __name__ == "__main__":
    solve_day2()
