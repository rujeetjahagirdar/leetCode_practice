class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # brute force
#         n1 = len(nums1)
#         n2 = len(nums2)
#         if(n1>=n2):
#             for i in range(n1):
#                 if(nums[i:i+n2]==nums2):
                    
#         elif(n2>n1):
#             pass
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        if(n1>=n2):
            for i in nums1:
                if i in nums2 and i not in result:
                    result.append(i)
        else:
            for i in nums2:
                if i in nums1 and i not in result:
                    result.append(i)
        print(result)
        return result