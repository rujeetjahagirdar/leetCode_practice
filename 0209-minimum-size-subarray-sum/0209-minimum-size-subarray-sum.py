class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # for i in range(1, len(nums)+1):
        #     sm = sum(nums[:i])
        #     # print(nums[:i], sm)
        #     if(sm>=target):
        #         return i
        #     for j in range(1,len(nums)-i+1):
        #         # print(nums[j:j+i])
        #         # if(sum(nums[j:j+i])>=target):
        #         #     return i
        #         sm = (sm - nums[j-1]) + nums[j+i-1]
        #         # print(nums[j:j+i],sm)
        #         if(sm>=target):
        #             return i
        # return 0
        ans = float("inf")
        left = right = 0
        current_sum = 0
        while(right<len(nums)):
            current_sum +=nums[right]
            while(current_sum>=target):
                ans = min(ans, right+1-left)
                current_sum -=nums[left]
                left +=1
            right +=1
        # print(ans)
        return ans if ans!=float('inf') else 0