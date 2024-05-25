class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(low, mid, high):
            left = low
            right = mid + 1
            util = []
            while left <= mid and right <= high:
                if nums[left] < nums[right]:
                    util.append(nums[left])
                    left += 1
                else:
                    util.append(nums[right])
                    right += 1
            while left <= mid:
                util.append(nums[left])
                left += 1
            while right <= high:
                util.append(nums[right])
                right += 1
            for i in range(len(util)): nums[low + i] = util[i]

        def merge_sort(low, high):
            if low >= high: return
            mid = low + (high - low) // 2
            merge_sort(low, mid)
            merge_sort(mid + 1, high)
            merge(low, mid, high)

        merge_sort(0, len(nums) - 1)
        return nums