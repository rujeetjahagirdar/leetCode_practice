class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        freq = Counter()
        first_occ = {}
        last_occ = {}

        for i in range(len(nums)):
            freq[nums[i]]+=1

            if(nums[i] not in first_occ):
                first_occ[nums[i]]=i
            
            last_occ[nums[i]]=i

        
        degree_arr = max(freq.values())
        ans=len(nums)

        for n in freq:
            if(freq[n]==degree_arr):
                ans = min(ans, (last_occ[n] - first_occ[n])+1)

        return ans        
        
        
        # freq = Counter(nums)
        # degree_arr = max(freq.values())

        # l=0
        # r=len(nums)-1

        # while(max(freq.values())==degree_arr):
        #     freq[nums[r]]-=1
        #     r-=1
        
        # r+=1
        # freq[nums[r]]+=1

        # while(max(freq.values())==degree_arr):
        #     freq[nums[l]]-=1
        #     l+=1
        
        # l-=1

        # return((r-l)+1)
