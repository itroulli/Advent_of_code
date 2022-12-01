import re


with open("inputs/day_06.txt", encoding="utf-8") as f:
    instructions = f.readlines()


def solve_day6(part_2=False):
    # Construct light grid
    lights = [[0 for i in range(1000)] for j in range(1000)]

    for instruction in instructions:
        # Parse instruction
        if "on" in instruction:
            action = "on"
        elif "off" in instruction:
            action = "off"
        if "toggle" in instruction:
            action = "toggle"

        coords_regex = re.compile(r"([0-9,]*) through ([0-9,]*)")
        first_coords = coords_regex.search(instruction).group(1)
        last_coords = coords_regex.search(instruction).group(2)
        first_x = int(first_coords.split(",")[0])
        last_x = int(last_coords.split(",")[0])
        first_y = int(first_coords.split(",")[1])
        last_y = int(last_coords.split(",")[1])
        if part_2:
            for x in range(first_x, last_x + 1):
                for y in range(first_y, last_y + 1):
                    lights[x][y] = (
                        lights[x][y] + 1
                        if action == "on"
                        else (
                            max(lights[x][y] - 1, 0)
                            if action == "off"
                            else lights[x][y] + 2
                        )
                    )
        else:
            for x in range(first_x, last_x + 1):
                for y in range(first_y, last_y + 1):
                    lights[x][y] = (
                        1
                        if action == "on"
                        else (0 if action == "off" else abs(lights[x][y] - 1))
                    )
    return sum([sum(lrow) for lrow in lights])


if __name__ == "__main__":
    print(f"Answer to part 1: {solve_day6()}")
    print(f"Answer to part 2: {solve_day6(part_2=True)}")
