class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # At index i, if the maximum value seen so far equals i, then all elements up to i can be sorted independently and will end up exactly in positions 0 â¦ i.

# That means we can safely end a chunk at index i.

        ans=0
        maxSoFar=0

        for i in range(len(arr)):
            maxSoFar = max(maxSoFar, arr[i])
            if(maxSoFar==i):
                ans+=1
        
        print(ans)
        return ans