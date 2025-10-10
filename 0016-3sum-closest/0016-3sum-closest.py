class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        #[-4,-1,1,2]

        closet_sum = float("inf")

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1

            while l<r:
                current_sum = nums[i]+nums[l]+nums[r]

                if(current_sum==target):
                    return current_sum

                if(abs(current_sum-target)<abs(closet_sum-target)):
                    closet_sum = current_sum

                if(current_sum<target):
                    l+=1
                else:
                    r-=1
                # print(closet_sum)
        
        return closet_sum