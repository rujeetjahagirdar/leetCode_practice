class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=-1
        mxFreq=0

        hashM = {}

        for i in nums:
            if(i not in hashM):
                hashM[i]=1
            else:
                hashM[i]+=1
            
            if(hashM[i]>mxFreq):
                ans=i
                mxFreq = hashM[i]
        
        return ans