class ArrayReader:
   def get(self, index: int) -> int:
       ...

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 10 ** 5
        while left <= right:
            mid = left + (right - left) // 2
            num = reader.get(mid)
            if num == 2 ** 31 - 1:
                right = mid - 1
            if num == target: return mid
            if num < target: left = mid + 1
            else: right = mid - 1
        return -1