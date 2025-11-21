class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        #two pointer

        nums.sort()
        closest_sum = float("inf")

        for i in range(len(nums)):
            n1 = nums[i]

            l=i+1
            r = len(nums)-1

            while(l<r):
                current_sum = n1 + nums[l]+nums[r]

                if(current_sum==target):
                    return current_sum

                if(abs(target-current_sum)<abs(closest_sum-target)):
                    closest_sum = current_sum
                
                if(current_sum<target):
                    l+=1
                else:
                    r-=1
        
        return(closest_sum)