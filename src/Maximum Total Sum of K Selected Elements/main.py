from heapq import heapify, heappop, heappush


class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        total_sum = 0
        nums = list(map(lambda num: - num, nums))
        heapify(nums)
        while k > 0:
            largest_number = -heappop(nums)
            if mul * largest_number > largest_number:
                total_sum += mul * largest_number
            else: total_sum += largest_number
            mul -= 1
            k -= 1
        return total_sum
