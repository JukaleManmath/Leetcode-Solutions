class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        key_arr = self.store.get(key, [])
        l , r = 0 , len(key_arr) - 1
        while(l <= r):
            mid = ( l + r)// 2
            if key_arr[mid][0] <= timestamp:
                res = key_arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)