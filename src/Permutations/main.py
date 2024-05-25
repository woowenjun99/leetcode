class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        responses = []

        def backtracking(start):
            if start == len(nums):
                responses.append(nums.copy())
                return
            for index in range(start, len(nums)):
                nums[index], nums[start] = nums[start], nums[index]
                backtracking(start + 1)
                nums[index], nums[start] = nums[start], nums[index]

        backtracking(0)
        return responses