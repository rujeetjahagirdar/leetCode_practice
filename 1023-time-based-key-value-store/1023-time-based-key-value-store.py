class TimeMap:

    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = []
        self.tm[key].append([value, timestamp])
        # print(self.tm)

    def get(self, key: str, timestamp: int) -> str:
        ans=""
        values = self.tm.get(key, [])
        l,r = 0, len(values)-1
        while(l<=r):
            m = (l+r)//2
            if(values[m][1]<=timestamp):
                ans = values[m][0]
                l=m+1
            else:
                r = m-1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)