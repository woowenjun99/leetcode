class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        matrix = [[""] * cols for _ in range(rows)]
        count = 0
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = encodedText[count]
                count += 1
        
        answer = []
        for col in range(cols):
            count = 0
            while col + count < cols and count < rows:
                answer.append(matrix[count][col + count])
                count += 1
        while answer and answer[-1] == " ": answer.pop()
        return "".join(answer)