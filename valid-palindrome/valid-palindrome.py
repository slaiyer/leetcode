class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        
        for idx in range(len(s) // 2):
            if s[idx] != s[len(s) - 1 - idx]:
                return False

        return True
