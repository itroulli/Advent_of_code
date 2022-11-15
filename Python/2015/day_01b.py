with open("inputs/day_01.txt") as text:
    input = text.read()

floor = 0

for pos, cmd in enumerate(input, 1):
    if cmd == "(":
        floor += 1
    elif cmd == ")":
        floor -= 1
    if floor < 0:
        break
print(pos)