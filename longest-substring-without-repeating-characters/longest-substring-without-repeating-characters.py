class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        chars = [-1] * 128
        start = -1
        max_len = 1

        for i in range(n):
            c = ord(s[i])
            i_prev = chars[c]
            chars[c] = i
            start = max(i_prev, start)
            max_len = max(i - start, max_len)

        return max_len
