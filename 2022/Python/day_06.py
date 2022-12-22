import os

PARENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
INPUT = os.path.join(PARENT_DIR, "inputs", "day_06.txt")


def window(fseq, window_size=4):
    for i in range(len(fseq) - window_size + 1):
        yield (i + window_size, fseq[i : i + window_size])


def solve_day6(part_two=False):
    with open(INPUT, encoding="utf-8") as text:
        input_text = text.read()
    # input_text = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    if part_two:
        for i, segment in window(input_text, 14):
            if len(set(segment)) == 14:
                print(f"The answer for part 2 is {i}")
    else:
        for i, segment in window(input_text, 4):
            if len(set(segment)) == 4:
                print(f"The answer for part 1 is {i}")
                break


if __name__ == "__main__":
    solve_day6()
    solve_day6(part_two=True)
