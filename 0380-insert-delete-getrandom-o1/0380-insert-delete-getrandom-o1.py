class RandomizedSet:

    def __init__(self):
        self.hashM = {}
        self.rSet = []
        

    def insert(self, val: int) -> bool:
        if(val in self.hashM):
            return False
        self.rSet.append(val)
        self.hashM[val] = len(self.rSet)-1

        return True

    def remove(self, val: int) -> bool:
        if(val not in self.hashM):
            return False
        idx = self.hashM[val]
        self.rSet[idx], self.rSet[-1] = self.rSet[-1], self.rSet[idx] #exchange to have fast remove
        self.hashM[self.rSet[idx]] = idx

        del self.hashM[self.rSet[-1]]
        del self.rSet[-1]

        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.rSet)-1)
        return self.rSet[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()