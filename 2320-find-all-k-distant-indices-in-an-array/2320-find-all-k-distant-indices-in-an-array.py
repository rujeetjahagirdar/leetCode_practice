class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans=[]

        r=0

        for i in range(len(nums)):
            if(nums[i]==key):
                l = max(r, i-k)
                r = min(len(nums)-1, i+k) +1

                for j in range(l, r):
                    ans.append(j)
        
        return(ans)