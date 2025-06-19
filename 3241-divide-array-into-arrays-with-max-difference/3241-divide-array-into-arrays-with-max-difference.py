class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans=[]

        nums.sort()
        # print(nums)
        for i in range(0,len(nums), 3):
            print(i)
            if(nums[i+2]-nums[i] <= k):
                ans.append(nums[i:i+3])
            else:
                return []
        return(ans)