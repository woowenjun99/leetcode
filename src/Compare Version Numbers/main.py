class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))
        max_length = max(len(version1), len(version2))
        version1 += [0] * (max_length - len(version1))
        version2 += [0] * (max_length - len(version2))
        left = right = 0
        while left < len(version1) and right < len(version2):
            if version1[left] == version2[right]: 
                left += 1
                right += 1
                continue
            if version1[left] < version2[right]: return -1
            else: return 1
        return 0