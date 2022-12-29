import os
import itertools

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_08.txt")


def solve_day8():
    with open(INPUT, encoding="utf-8") as text:
        input_text = text.read().splitlines()
        matrix = [[int(x) for x in row] for row in input_text]
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    visible = 2 * n_rows + 2 * n_cols - 4
    max_score = 0
    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            score = 1
            tree = matrix[i][j]
            right = matrix[i][j + 1 :]
            left = list(reversed(matrix[i][:j]))
            down = [matrix[k][j] for k in range(i + 1, n_rows)]
            up = [matrix[k][j] for k in range(i - 1, -1, -1)]
            directions = (right, left, down, up)
            if any([tree > max(direction) for direction in (right, left, down, up)]):
                visible += 1
            for direction in directions:
                dir_score = 0
                for t in direction:
                    dir_score += 1
                    if t >= tree:
                        break
                score *= dir_score
            if score > max_score:
                max_score = score
    print(f"Answer to part 1: {visible}")
    print(f"Answer to part 2: {max_score}")


if __name__ == "__main__":
    solve_day8()
