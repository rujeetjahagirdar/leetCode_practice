class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = float('-inf')
        window = set()
        windowSum=0
        l=0

        for r in range(len(nums)):
            if(nums[r] not in window):
                window.add(nums[r])
                windowSum+=nums[r]
                ans = max(ans, windowSum)
                # print(window)
                print(ans)
            else:
                while(nums[l]!=nums[r]):
                    window.remove(nums[l])
                    windowSum-=nums[l]
                    l+=1
                    
                    # print(window)
                # window.remove(nums[l])
                l+=1
                # print(window)
        print(ans)
        return ans
            
