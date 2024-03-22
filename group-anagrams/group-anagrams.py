class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, list[str]] = defaultdict(list)

        for s in strs:
            sig = [0] * 26

            for c in s:
                sig[ord(c) - ord('a')] += 1

            groups[tuple(sig)].append(s)

        return groups.values()
