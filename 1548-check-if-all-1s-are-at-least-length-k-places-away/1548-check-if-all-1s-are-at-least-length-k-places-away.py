class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_idx = -1

        for i in range(len(nums)):
            if(nums[i]==1):
                if(last_idx==-1):
                    last_idx=i
                else:
                    if((i-last_idx)<=k):
                        return False
                    last_idx=i
        
        return True