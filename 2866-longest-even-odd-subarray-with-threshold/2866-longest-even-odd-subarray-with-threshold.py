class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        l=0

        while(l<len(nums)):
            if(nums[l]%2==0 and nums[l]<=threshold):
                print("l=", nums[l])
                tMax = 1
                j=l+1
                while(j<len(nums)):
                    if(nums[j]%2!=nums[j-1]%2 and nums[j]<=threshold):
                        tMax+=1
                    else:
                        ans = max(tMax, ans)
                        print(ans)
                        # l=j
                        break
                    j+=1
                l=j
                ans = max(tMax, ans)
            else:
                l+=1
        print(ans)
        return ans