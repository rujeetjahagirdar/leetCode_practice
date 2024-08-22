class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        #use binary seach
            #if mid is greater than right and greater than left
                #return mid+1
            #if mid is gretaer than left and less than right
                # left = mid+1
            #if mid is less than right and greater then left
                #right = mid-1
        low = 0
        high = len(nums)-1
        ans=nums[0]
        print(low, high)
        while(low<=high):
            if(nums[low]<nums[high]):
                ans = min(ans, nums[low])
                break
            mid = (low+high)//2
            # print(low, high, mid)
            ans = min(ans, nums[mid])
            if(nums[mid]>=nums[low]):
                low = mid+1
            else:
                high = mid-1
        print(ans)
        return ans