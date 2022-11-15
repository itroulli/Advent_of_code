with open("inputs/day_03.txt") as text:
    input_text = text.read()
    
def move(cmd: str, pos: tuple):
    commands = {"^": (0,1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}
    return tuple(sum(x) for x in zip(commands[cmd], pos))  

pos = (0,0)
robo_pos = (0,0)
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
      
print(len(visited))