from collections import deque

if __name__ == "__main__":
    with open("in.txt", "r+") as f: lines = f.readlines()
    lines = "".join(lines)

    answer = 0
    candidates = []
    enabled = True
    for i in range(len(lines)):
        if lines[i:i+7] == "don't()":
            enabled = False
            continue
        if lines[i:i+4] == "do()":
            enabled = True
            continue
        if lines[i:i+4] != "mul(" or not enabled: continue
        line = deque(lines[i+4:i+12])
        while line and line[-1] != ")": line.pop()
        while line and line[-1] == ")": line.pop()
        if not line: continue
        candidates.append("".join(line))

    for candidate in candidates:
        candidate = "".join(candidate).split(",")
        if len(candidate) != 2 or not candidate[0].isnumeric() or not candidate[1].isnumeric(): continue
        candidate = list(map(int, candidate))
        answer += candidate[0] * candidate[1]
    print(answer)