from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        counter = sorted([(counter[key], key) for key in counter.keys()], reverse=True)
        response = ""
        for freq, key in counter: response += key * freq
        return response