from itertools import combinations
from operator import mul

with open("inputs/day_02.txt") as text:
    input_text = text.readlines()

total = 0

for package in input_text:
    size = list(map(int, package.split("x")))
    package_ribbon = [2*x + 2*y for x,y in combinations(size, 2)]
    extra = 1
    for dim in size:
        extra = mul(dim, extra)
    total += min(package_ribbon) + extra

print(total)