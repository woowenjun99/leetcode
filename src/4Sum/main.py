from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = set()
        
        for i in range(len(nums) - 3):
            if i - 1 >= 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                two_sum_target = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] == two_sum_target:
                        results.add(tuple(sorted([nums[i], nums[j], nums[left], nums[right]])))
                        left += 1
                    elif nums[left] + nums[right] < two_sum_target:
                        left += 1
                    else:
                        right -= 1
                        
        return list([list(result) for result in results])
    
print(Solution().fourSum([1,0,-1,0,-2,2], 0))