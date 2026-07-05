class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        for c in t:
            if c in dict:
                dict[c] -= 1
            else:
                return False
        for (key, value) in dict.items():
            if value != 0:
                return False
        return True
        