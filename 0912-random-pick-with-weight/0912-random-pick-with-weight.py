class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]

        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1]+w[i])
        

    def pickIndex(self) -> int:
        randNum = random.randint(1, self.prefix[-1])

        for i in range(len(self.prefix)):
            if(self.prefix[i]>=randNum):
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()