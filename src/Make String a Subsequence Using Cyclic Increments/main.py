class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        last_change = None
        left = right = 0

        while left < len(str1) and right < len(str2):
            if last_change is not None and last_change - left > 1 and str1[left] != str2[right]: return False
            
            # If the left pointer and right pointer are the same we can advance both
            if str1[left] == str2[right]:
                right += 1
            # If both pointer are different but we have not changed the element before or the change was 1 element ago, we can change it and advance both pointers too
            # We update the last change to be left so that we know we can change the next element in the next iteration
            elif chr((ord(str1[left]) - ord("a") + 1) % 26 + ord("a")) == str2[right]:
                right += 1
                last_change = left
            left += 1
        return right == len(str2)
