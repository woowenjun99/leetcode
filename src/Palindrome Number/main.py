class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        temp = 0
        cloned = x
        while cloned > 0:
            temp = temp * 10 + cloned % 10
            cloned //= 10
        return temp == x
        