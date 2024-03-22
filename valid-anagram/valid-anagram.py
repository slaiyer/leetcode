from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurences: dict[str, int] = defaultdict(int)
        
        for idx in range(len(s)):
            occurences[s[idx]] += 1
            occurences[t[idx]] -= 1

        for v in occurences.values():
            if v != 0:
                return False

        return True
