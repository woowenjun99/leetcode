class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        answer = []
        count = horizontal = vertical = 0

        while len(answer) < (len(matrix) * len(matrix[0])):
            while vertical < len(matrix[0]) and not visited[horizontal][vertical]:
                visited[horizontal][vertical] = True
                answer.append(matrix[horizontal][vertical])
                vertical += 1
            vertical -= 1
            horizontal += 1
            while horizontal < len(matrix) and not visited[horizontal][vertical]:
                visited[horizontal][vertical] = True
                answer.append(matrix[horizontal][vertical])
                horizontal += 1
            horizontal -= 1
            vertical -= 1
            while vertical >= 0 and not visited[horizontal][vertical]:
                visited[horizontal][vertical] = True
                answer.append(matrix[horizontal][vertical])
                vertical -= 1
            vertical += 1
            horizontal -= 1
            while horizontal >= 0 and not visited[horizontal][vertical]:
                visited[horizontal][vertical] = True
                answer.append(matrix[horizontal][vertical])
                horizontal -= 1
            horizontal += 1
            vertical += 1

        return answer