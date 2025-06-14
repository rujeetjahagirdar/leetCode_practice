class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans=0
        # uniques = set()
        # for i in nums:
        #     if(i in uniques):
        #         j=1
        #         while(j<len(nums) and (i+j) in uniques):
        #             ans+=1
        #             j+=1
        #         ans+=1
        #         uniques.add(i+j)
        #     else:
        #         uniques.add(i)
        
        # print(ans)
        # print(uniques)
        # return ans

        nums.sort()
        # print(nums)
        for i in range(1, len(nums)):
            if(nums[i]<=nums[i-1]):
                ans+=(nums[i-1]-nums[i])+1
                nums[i]+=(nums[i-1]-nums[i])+1
                
        
            # print(nums)
        return(ans)