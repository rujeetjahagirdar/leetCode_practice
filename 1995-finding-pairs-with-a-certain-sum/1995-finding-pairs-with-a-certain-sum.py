class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.count1 = Counter(nums1)
        self.count2 = Counter(nums2)
        # self.nums1 = nums1
        self.nums2 = nums2
        # self.mults = defaultdict(int)

        # for c1 in self.count1:
        #     for c2 in self.count2:
        #         self.mults[c1*c2]+=1

    def add(self, index: int, val: int) -> None:
        self.count2[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.count2[self.nums2[index]]+=1

    def count(self, tot: int) -> int:
        ans=0
        for c1 in self.count1:
            if((tot - c1) in self.count2):
                ans+= self.count1[c1] * self.count2[(tot - c1)]
            
        return ans



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)