class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        # use freq count approach

        diffs = [abs(nums1[i]-nums2[i]) for i in range(len(nums1))]
        max_diff = max(diffs)

        diff_freq = [0] * (max_diff+1)

        for d in diffs:
            diff_freq[d]+=1
        
        k = k1+k2

        if(sum(diffs)<=k):
            return 0

        
        for d in range(max_diff, 0, -1):
            if(diff_freq[d]==0):
                continue
            
            if(k>=diff_freq[d]):
                k-=diff_freq[d]
                diff_freq[d-1] +=diff_freq[d]
                diff_freq[d]=0
            else:
                diff_freq[d]-=k
                diff_freq[d-1]+=k
                k=0
                break
        
        ans=0

        for i in range(len(diff_freq)):
            if(diff_freq[i]>0):
                ans+=(i*i)* diff_freq[i]

        return(ans)
        
        
        # # use max-heap

        # diffs = [abs(nums1[i]-nums2[i]) for i in range(len(nums1))]

        # max_heap = [-d for d in diffs]

        # k=k1+k2

        # if sum(diffs) <= k:
        #     return 0

        # heapq.heapify(max_heap)

        

        # # print(max_heap)

        # while(k>0):
        #     max_diff = -heapq.heappop(max_heap)

        #     # print(max_heap)

        #     if(max_diff==0):
        #         break

        #     max_diff-=1

        #     heapq.heappush(max_heap, -max_diff)
        #     k-=1
        
        # ans=0

        # for d in max_heap:
        #     ans+= (-d)**2
        
        # return(ans)
        
        

