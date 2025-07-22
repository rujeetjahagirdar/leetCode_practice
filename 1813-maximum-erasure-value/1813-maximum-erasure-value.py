class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = float('-inf')
        window = set()

        l=0

        for r in range(len(nums)):
            if(nums[r] not in window):
                window.add(nums[r])
                ans = max(ans, sum(window))
                # print(window)
                print(ans)
            else:
                while(nums[l]!=nums[r]):
                    window.remove(nums[l])
                    l+=1
                    
                    # print(window)
                # window.remove(nums[l])
                l+=1
                # print(window)
        print(ans)
        return ans
            
