class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        num_count = defaultdict(int)
        ans=0
        mod = 10**9 + 7

        for i in nums:
            num_count[i]+=1
        
        left_count_till_now = defaultdict(int)

        for i in nums:
            target = 2*i
            left_count = left_count_till_now.get(target, 0)

            if(i==target):
                right_count = num_count.get(target, 0)-1 - left_count
            else:
                right_count = num_count.get(target, 0) - left_count
            
            ans = (ans+left_count * right_count) %mod

            left_count_till_now[i]+=1
        
        return(ans)