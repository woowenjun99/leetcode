if __name__ == "__main__":
    with open("in.txt", "r+") as f: lines = f.readlines()
    for index in range(len(lines)): lines[index] = list(lines[index].removesuffix("\n"))
    answer = 0
    for row in range(len(lines) - 2):
        for col in range(len(lines[row]) - 2):
            if lines[row][col] == lines[row + 2][col] == "M" and lines[row + 1][col + 1] == "A" and lines[row][col + 2] == lines[row + 2][col + 2] == "S":
                answer += 1
            elif lines[row + 2][col] == lines[row + 2][col + 2] == "M" and lines[row + 1][col + 1] == "A" and lines[row][col] == lines[row][col + 2] == "S":
                answer += 1
            elif lines[row][col + 2] == lines[row + 2][col + 2] == "M" and lines[row + 1][col + 1] == "A" and lines[row][col] == lines[row + 2][col] == "S":
                answer += 1
            elif lines[row][col] == lines[row][col + 2] == "M" and lines[row + 1][col + 1] == "A" and lines[row + 2][col] == lines[row + 2][col + 2] == "S":
                answer += 1
    print(answer)