class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums)==1):
            if nums[0]!=target:
                return -1
        
        l=0
        r = len(nums)-1
        ans=-1

        while(l<=r):
            mid = (l+r)//2
            # print(nums[l], nums[r], nums[mid])

            if(nums[mid]==target):
                return mid
            
            if(nums[l]<=nums[mid]):
                if(nums[l]<=target<nums[mid]):
                    r = mid-1
                else:
                    l=mid+1
            else:
                if(nums[mid]<target<=nums[r]):
                    l=mid+1
                else:
                    r = mid-1
            
        return -1