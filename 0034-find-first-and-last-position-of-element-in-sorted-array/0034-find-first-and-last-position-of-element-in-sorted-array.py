class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[]

        idx = -1

        l=0
        r=len(nums)-1

        while(l<=r):
            mid = l + (r-l)//2

            if(nums[mid]==target):
                idx = mid
                r = mid-1
            elif(target>nums[mid]):
                l=mid+1
            else:
                r = mid-1
        print(idx)

        ans.append(idx)

        idx=-1

        l=0
        r=len(nums)-1

        while(l<=r):
            mid = l + (r-l)//2

            if(nums[mid]==target):
                idx = mid
                l=mid+1
            elif(target>nums[mid]):
                l=mid+1
            else:
                r = mid-1
        print(idx)
        ans.append(idx)

        return ans