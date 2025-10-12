class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            return nums2
        if not nums2:
            return nums2
        
        i = m-1
        j = n-1
        k = len(nums1)-1

        while(j>=0):
            if(nums2[j]>=nums1[i]):
                nums1[k]=nums2[j]
                j-=1
                k-=1
            else:
                nums1[k] = nums1[i]
                k-=1
                i-=1
        return nums1
            