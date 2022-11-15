from collections import Counter

with open("inputs/day_01.txt") as text:
    input_text = text.read()
    
cnt = Counter(input_text)

print(cnt["("] - cnt[")"])
