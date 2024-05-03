from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map: dict[int, int] = defaultdict(int)

        for i in nums:
            freq_map[i] += 1

        heap = [(v, k) for k, v in freq_map.items()]
        heapq.heapify(heap)

        return [t[1] for t in heapq.nlargest(k, heap)]
