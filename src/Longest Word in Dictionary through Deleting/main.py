from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        results = []

        for word in dictionary:
            if len(word) > len(s) or (len(word) == len(s) and s != word): continue
            left = right = 0
            while left < len(s) and right < len(word):
                if s[left] == word[right]: right += 1
                left += 1
            if right == len(word): results.append(word)

        results.sort()
        longest_word = ""
        for result in results:
            if len(result) > len(longest_word): longest_word = result
        return longest_word