class Solution:
    def mirrorDistance(self, n: int) -> int:
        stack = []
        original = n
        while n > 0:
            stack.append(n % 10)
            n //= 10
        reverse = 0
        for i in range(len(stack)): reverse = reverse * 10 + stack[i]
        return abs(original - reverse)