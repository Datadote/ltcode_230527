class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.store.get(key, [])
        L, R = 0, len(values)-1
        while L <= R:
            M = L + (R-L)//2
            if values[M][1] <= timestamp:
                res = values[M][0]
                L = M + 1
            else:
                R = M - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)