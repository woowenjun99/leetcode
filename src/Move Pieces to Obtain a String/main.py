class Solution:
    def canChange(self, start: str, target: str) -> bool:
        end_stack, start_stack = [], []
        for index, element in enumerate(start): 
            if element == "_": continue
            start_stack.append((element, index))
        for index, element in enumerate(target):
            if element == "_": continue
            end_stack.append((element, index))

        # In the event that that the number of L and R in total do not match for both stack, we return False
        if len(start_stack) != len(end_stack): return False
        
        # We check if the L matches L and R matches R in both stacks. If they don't match, return False
        # We check if the end position of L is greater than initial position. If yes, return False because we can only move left.
        # Likewise for R
        for s, e in zip(start_stack, end_stack):
            if s[0] != e[0] or (s[0] == "L" and e[1] > s[1]) or (s[0] == "R" and e[1] < s[1]): return False
        return True
