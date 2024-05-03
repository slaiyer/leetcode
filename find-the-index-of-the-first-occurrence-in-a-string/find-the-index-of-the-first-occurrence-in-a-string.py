class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for idx in range(0, len(haystack) - len(needle) + 1):
            if needle == haystack[idx : idx + len(needle)]:
                return idx

        return -1
