import os

# Step 1: Get all the questions that we have attempted
subdirectories = os.walk("src")
questions_solved = list(subdirectories)[0][1]
questions_solved.sort()

# Step 2: Build the table
with open("README.md", "w+") as f:
    f.write("# Leetcode\n\n")
    f.write(f"## Total questions solved: {len(questions_solved)}\n\n")
    f.write("|Question|\n")
    f.write("|:---:|\n")
    for question in questions_solved: f.write(f"|{question}|\n")