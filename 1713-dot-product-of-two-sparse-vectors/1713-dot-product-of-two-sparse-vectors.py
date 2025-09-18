class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.values = {}

        for i in range(len(nums)):
            if(nums[i]!=0):
                self.values[i] = nums[i]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        self.ans = 0
        # print(vec.values)
        # print(self.values)
        
        for i in vec.values:
            if(i in self.values):
                self.ans+=self.values[i]*vec.values[i]
        
        return(self.ans)
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)