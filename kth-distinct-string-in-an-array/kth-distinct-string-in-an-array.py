from collections import defaultdict


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        d: dict[str, int] = defaultdict(int)
        for s in arr:
            d[s] += 1

        count = 0
        for s, c in d.items():
            if c == 1:
                if count == k - 1:
                    return s
                count += 1

        return ""
