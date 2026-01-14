class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # nums_set = set(nums)
        # ans=0

        # for i in nums_set:
        #     if(i-1 not in nums_set):
        #         curr = i
        #         curr_len=1

        #         while(curr+1 in nums_set):
        #             curr_len+=1
        #             curr+=1
        #         ans=max(ans, curr_len)
        
        # print(ans)
        # return ans

        numsSet = set(nums)
        currlen = 0
        ans=0

        for n in numsSet:
            if(n-1 not in numsSet): #this avoids re-processing same elements again
                currN = n
                currlen=1

                while(currN+1 in numsSet):
                    currlen+=1
                    currN+=1
                ans=max(ans, currlen)
        
        return ans