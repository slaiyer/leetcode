from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.d: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        vals = self.d[key]
        left, right = 0, len(vals) - 1
        res = ""
        while left <= right:
            mid = left + (right - left) // 2
            midts = vals[mid][0]

            if midts <= timestamp:
                res = vals[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
