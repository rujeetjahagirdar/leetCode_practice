class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)-1):
            if((nums[i+1]-nums[i])-1>=k):
                return nums[i]+k
            else:
                k-=((nums[i+1]-nums[i])-1)
        return nums[-1]+k



        l=0
        r = len(nums)-1

        while(l<=r):
            mid = l + (r-l)//2

            noOfMissings = (nums[mid] - nums[0])-mid

            if(noOfMissings<k):
                return nums[mid]+(k-noOfMissings)
            else:
                r = mid
        return nums[-1] + (k - (nums[-1]-nums[0])-len(nums)-1)