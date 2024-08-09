class TimeMap:

    def __init__(self):
        self.d: dict[str, dict[int, str]] = defaultdict(lambda: defaultdict())

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        for t in reversed(self.d[key]):
            if t <= timestamp:
                return self.d[key][t]

        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)