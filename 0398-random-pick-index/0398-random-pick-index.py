class Solution:

    def __init__(self, nums: List[int]):
        self.hashM = defaultdict(list)

        for i in range(len(nums)):
            if(nums[i] in self.hashM):
                self.hashM[nums[i]].append(i)
            else:
                self.hashM[nums[i]] = [i]
        
        # print(self.hashM)
        

    def pick(self, target: int) -> int:
        if(target in self.hashM):
            return random.choice(self.hashM[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)