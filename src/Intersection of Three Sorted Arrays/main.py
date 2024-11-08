from typing import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        stack = []
        left = right = 0
        while left < len(arr1) and right < len(arr2):
            if arr1[left] == arr2[right]:
                stack.append(arr1[left])
                left += 1
                right += 1
                continue
            if arr1[left] < arr2[right]:
                left += 1
            else:
                right += 1
        answer = []
        left = right = 0
        while left < len(stack) and right < len(arr3):
            if stack[left] == arr3[right]:
                answer.append(stack[left])
                left += 1
                right += 1
                continue
            if stack[left] < arr3[right]: left += 1
            else: right += 1
        return answer
