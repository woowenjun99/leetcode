from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted([candidate for candidate in candidates if candidate <= target])
        appeared = set()
        responses = []
        
        def backtracking(start, total, used_values):
            if total >= target:
                if total == target and tuple(sorted(used_values)) not in appeared: 
                    appeared.add(tuple(sorted(used_values)))
                    responses.append(used_values.copy())
                return
            
            for index in range(len(candidates)):
                used_values.append(candidates[index])
                backtracking(start + 1, total + candidates[index], used_values)
                used_values.pop()
                
        backtracking(0, 0, [])
        return responses