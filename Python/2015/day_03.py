def move(cmd: str, pos: tuple):
    commands = {"^": (0, 1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}
    return tuple(sum(x) for x in zip(commands[cmd], pos))


def solve_day3(part_two=False):
    with open("inputs/day_03.txt") as text:
        input_text = text.read()
    if part_two:
        pos = (0, 0)
        robo_pos = (0, 0)
        visited = set([pos])
        robo_turn = False
        print(visited)
        for c in input_text:
            if robo_turn:
                robo_pos = move(c, robo_pos)
                visited.add(robo_pos)
                robo_turn = False
            else:
                pos = move(c, pos)
                visited.add(pos)
                robo_turn = True

        print(f"Answer for part 2: {len(visited)}")
    else:
        position = (0, 0)
        at_least_one = set([position])

        for c in input_text:
            position = move(c, position)
            at_least_one.add(position)

        print(f"Answer for part 1: {len(at_least_one)}")


if __name__ == "__main__":
    solve_day3()
    solve_day3(part_two=True)
