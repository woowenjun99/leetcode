from typing import List

def is_increasing_or_decreasing(nums: List[int]):
    is_increasing = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]: is_increasing = False
    if is_increasing: return True
    is_decreasing = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]: is_decreasing = False
    return is_decreasing

def check_difference(nums: List[int]):
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) < 1 or abs(nums[i] - nums[i - 1]) > 3: return False
    return True
    
with open("in.txt", "r+") as f: 
    lines = f.readlines()
    answer = 0
    for index in range(len(lines)): lines[index] = list(map(int, lines[index].split()))
    for line in lines:
        combinations = []
        for i in range(len(line)):
            combination = []
            for j in range(len(line)):
                if i == j: continue
                combination.append(line[j])
            combinations.append(combination)
        is_answer = 0
        for combination in combinations:
            if is_increasing_or_decreasing(combination) and check_difference(combination): 
                is_answer = 1
        answer += is_answer
    print(answer)