from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result =[]
#         n1 = len(nums1)
#         n2 = len(nums2)
#         if(n1>n2):
#             for i in nums2:
#                 if i in nums1:
#                     result.append(i)
#         else:
#             for i in nums1:
#                 if i in nums2:
#                     result.append(i)
        
#         return result
#         # for i in nums1:
#         #     if i in nums2:
#         #         result.append(i)
#         # print(result)
#         # return result
        return(list((Counter(nums1) & Counter(nums2)).elements()))