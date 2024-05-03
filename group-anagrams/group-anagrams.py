from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups: dict[tuple[int, ...], list[str]] = defaultdict(list)

        for s in strs:
            sig = [0] * 26

            for c in s:
                sig[ord(c) - ord("a")] += 1

            groups[tuple(sig)].append(s)

        return list(groups.values())
