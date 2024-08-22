class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        ans = float("inf")
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while(left<right):
                curr_sum = nums[i] + nums[left] + nums[right]
                if(abs(curr_sum - target)<abs(ans - target)):
                    ans = curr_sum
                
                if curr_sum==target:
                    return curr_sum
                if curr_sum>target:
                    right -=1
                if curr_sum<target:
                    left +=1
        return ans