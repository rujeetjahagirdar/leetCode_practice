class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            # print(i, idx)
            if(idx==len(nums2)-1):
                ans[i] = -1
            else:
                for j in range(idx+1, len(nums2)):
                    # print(j)
                    if(nums2[j]>nums1[i]):
                        ans[i] = nums2[j]
                        # print(ans)
                        break
                if(ans[i]==-1):
                    ans[i]=-1
            # print(ans)
        # print(ans)
        return ans