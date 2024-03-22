from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurences: dict[str, int] = defaultdict(int)
        
        for c in s:
            occurences[c] += 1

        for c in t:
            occurences[c] -= 1

        for v in occurences.values():
            if v != 0:
                return False

        return True
