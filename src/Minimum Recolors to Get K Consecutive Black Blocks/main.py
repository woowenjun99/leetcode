class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        answer = float("inf")
        for i in range(len(blocks) - k + 1): answer = min(answer, list(blocks[i:i+k]).count("W"))
        return answer
