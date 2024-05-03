class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = [c.lower() for c in s if c.isalnum()]

        for idx in range(len(s2) // 2):
            if s2[idx] != s2[len(s2) - 1 - idx]:
                return False

        return True
