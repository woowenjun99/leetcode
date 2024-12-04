from collections import Counter

with open("in.txt", "r+") as f: 
    lines = f.readlines()
    right = []
    for index in range(len(lines)): lines[index] = list(map(int, lines[index].split()))
    left = sorted(map(lambda x: x[0], lines))
    right = Counter(map(lambda x: x[1], lines))
total = 0
for l in left: total += l * right[l]
print(total)