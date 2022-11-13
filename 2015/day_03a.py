with open("inputs/day_03.txt") as text:
    input_text = text.read()
    
def move(cmd: str, pos: tuple):
    commands = {"^": (0,1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}
    return tuple(sum(x) for x in zip(commands[cmd], pos))  

position = (0,0)
at_least_one = set([position])

for c in input_text:
    position = move(c, position)
    at_least_one.add(position)
    
print(len(at_least_one))