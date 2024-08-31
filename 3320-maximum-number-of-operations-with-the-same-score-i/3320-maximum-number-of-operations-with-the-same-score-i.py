class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans =1
        score = (nums.pop(0)+nums.pop(0))
        while(len(nums)>=2):
            n1 = nums.pop(0)
            n2 = nums.pop(0)
            if(n1+n2==score):
                ans +=1
            else:
                break

        return ans