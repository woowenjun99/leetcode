class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maximum_visited = 0

        for i in range(len(nums)):
            if i > maximum_visited: return False        # We cannot jump beyond this point
            if nums[i] + i <= maximum_visited: continue # Optimization: Not improving
            maximum_visited = nums[i] + i

        return True