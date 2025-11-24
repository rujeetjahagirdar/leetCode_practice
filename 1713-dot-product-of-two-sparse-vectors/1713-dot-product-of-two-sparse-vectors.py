class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}

        for i in range(len(nums)):
            if(nums[i]!=0):
                self.vector[i] = nums[i]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if not self.vector or not vec:
            return 0

        ans=0

        for i in vec.vector:
            if(i in self.vector):
                ans+=vec.vector[i] * self.vector[i]
        
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)