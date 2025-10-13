class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #sum of subarray [i...j] would be (sum of subarry [0....j] - sum of subarray [0....i])
        #so we can use prefix sum to solve this problem

        #we will find sum of subarrays for all j [0...j] and maintain it in hashmap with their count
        #and check sum of subarray - k in this hashmap and increment ans

        hashM = {0: 1}
        sum_till_j = 0
        ans=0

        for j in range(len(nums)):
            sum_till_j += nums[j]

            if((sum_till_j - k) in hashM):
                ans+=hashM[(sum_till_j - k)]
            
            hashM[sum_till_j] = hashM.get(sum_till_j, 0) + 1
        
        return ans