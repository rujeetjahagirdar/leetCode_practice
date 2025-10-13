class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [nums[0]]

        for i in range(1, len(nums)):
            self.prefixSum.append(self.prefixSum[-1]+nums[i])
        
        #[-2, -2, 1, -4, -2, -3]

    def sumRange(self, left: int, right: int) -> int:
        if(left==0):
            return self.prefixSum[right]
        else:
            return (self.prefixSum[right] - self.prefixSum[left-1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)